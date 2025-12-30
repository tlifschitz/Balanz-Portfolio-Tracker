"""Authentication flow for Balanz API."""
import httpx
from typing import Optional
from .models import InitResponse, LoginResponse


class AuthenticationError(Exception):
    """Raised when authentication fails."""
    pass


class BalanzAuth:
    """Handles Balanz authentication flow."""

    BASE_URL = "https://clientes.balanz.com/api/v1"

    def __init__(self):
        self.access_token: Optional[str] = None
        self.user_info: Optional[LoginResponse] = None
        self._client = httpx.Client(timeout=30.0)

    def _get_headers(self, include_auth: bool = False) -> dict:
        """Get default headers for API requests."""
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Lang': 'es',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"'
        }

        if include_auth and self.access_token:
            headers['Authorization'] = self.access_token

        return headers

    async def init(self, username: str) -> str:
        """
        Initialize authentication flow.

        Args:
            username: Balanz username

        Returns:
            nonce: Authentication nonce for login

        Raises:
            AuthenticationError: If init fails
        """
        url = f"{self.BASE_URL}/auth/init?avoidAuthRedirect=true"
        payload = {
            "user": username,
            "source": "WebV2"
        }

        try:
            response = self._client.post(url, json=payload, headers=self._get_headers())
            response.raise_for_status()

            init_data = InitResponse(**response.json())
            return init_data.nonce

        except httpx.HTTPError as e:
            raise AuthenticationError(f"Failed to initialize authentication: {str(e)}")
        except Exception as e:
            raise AuthenticationError(f"Unexpected error during init: {str(e)}")

    async def login(self, username: str, password: str, nonce: str) -> LoginResponse:
        """
        Complete authentication and obtain access token.

        Args:
            username: Balanz username
            password: Balanz password (held in memory only during this call)
            nonce: Nonce from init call

        Returns:
            LoginResponse with user info and access token

        Raises:
            AuthenticationError: If login fails
        """
        url = f"{self.BASE_URL}/auth/login?avoidAuthRedirect=true"
        payload = {
            "user": username,
            "pass": password,
            "nonce": nonce,
            "source": "WebV2",
            "idDispositivo": "balanz-portfolio-tracker",
            "TipoDispositivo": "Web",
            "sc": 1,
            "Nombre": "Balanz Portfolio Tracker",
            "SistemaOperativo": "Desktop",
            "VersionSO": "1.0",
            "VersionAPP": "1.0.0"
        }

        try:
            response = self._client.post(url, json=payload, headers=self._get_headers())
            response.raise_for_status()

            login_data = LoginResponse(**response.json())

            # Store access token and user info in memory
            self.access_token = login_data.AccessToken
            self.user_info = login_data

            return login_data

        except httpx.HTTPError as e:
            raise AuthenticationError(f"Login failed: {str(e)}")
        except Exception as e:
            raise AuthenticationError(f"Unexpected error during login: {str(e)}")

    async def logout(self) -> None:
        """
        Logout and invalidate session token.
        Clears all session data from memory.
        """
        if not self.access_token:
            return

        url = f"{self.BASE_URL}/logout"

        try:
            response = self._client.post(
                url,
                json={},
                headers=self._get_headers(include_auth=True)
            )
            response.raise_for_status()

        except httpx.HTTPError:
            # Continue with cleanup even if API call fails
            pass
        finally:
            # Clear all session data from memory
            self.access_token = None
            self.user_info = None

    def is_authenticated(self) -> bool:
        """Check if user is currently authenticated."""
        return self.access_token is not None

    def get_token(self) -> Optional[str]:
        """Get current access token."""
        return self.access_token

    def get_user_info(self) -> Optional[LoginResponse]:
        """Get current user information."""
        return self.user_info

    def close(self):
        """Close HTTP client and cleanup."""
        self._client.close()
        self.access_token = None
        self.user_info = None
