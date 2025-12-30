"""Balanz API client wrapper."""
import httpx
from typing import Optional
from datetime import datetime
from .models import EstadoDeCuentaResponse, EvolucionDeCarteraResponse, FlujoProyectadoResponse
from .auth import BalanzAuth


class BalanzAPIError(Exception):
    """Raised when API calls fail."""
    pass


class BalanzClient:
    """Main client for interacting with Balanz API."""

    BASE_URL = "https://clientes.balanz.com/api/v1"

    def __init__(self, auth: BalanzAuth):
        """
        Initialize Balanz API client.

        Args:
            auth: Authenticated BalanzAuth instance
        """
        self.auth = auth
        self._client = httpx.Client(timeout=30.0)

    def _get_headers(self) -> dict:
        """Get headers with authentication token."""
        if not self.auth.is_authenticated():
            raise BalanzAPIError("Not authenticated. Please login first.")

        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Lang': 'es',
            'Authorization': self.auth.get_token(),
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"'
        }

    async def get_estado_de_cuenta(
        self,
        fecha: Optional[str] = None,
        ta: int = 1,
        id_moneda: int = 1
    ) -> EstadoDeCuentaResponse:
        """
        Get account statement with current holdings.

        Args:
            fecha: Date in YYYYMMDD format (defaults to today)
            ta: Account type (default 1)
            id_moneda: Currency ID (1=ARS, 2=USD)

        Returns:
            EstadoDeCuentaResponse with holdings, liquidity, and allocation

        Raises:
            BalanzAPIError: If API call fails
        """
        if not self.auth.user_info:
            raise BalanzAPIError("User info not available")

        if fecha is None:
            fecha = datetime.now().strftime("%Y%m%d")

        id_persona = self.auth.user_info.idPersona
        url = f"{self.BASE_URL}/estadodecuenta/{id_persona}"

        params = {
            "Fecha": fecha,
            "ta": ta,
            "idMoneda": id_moneda
        }

        try:
            response = self._client.get(url, params=params, headers=self._get_headers())
            response.raise_for_status()

            return EstadoDeCuentaResponse(**response.json())

        except httpx.HTTPError as e:
            raise BalanzAPIError(f"Failed to fetch account statement: {str(e)}")
        except Exception as e:
            raise BalanzAPIError(f"Unexpected error: {str(e)}")

    async def get_evolucion_de_cartera(
        self,
        fecha_desde: str,
        fecha_hasta: str,
        id_moneda: int = 2,
        tenencia: int = 1,
        eventos: int = 1
    ) -> EvolucionDeCarteraResponse:
        """
        Get portfolio evolution/performance over time.

        Args:
            fecha_desde: Start date in YYYYMMDD format
            fecha_hasta: End date in YYYYMMDD format
            id_moneda: Currency ID (1=ARS, 2=USD)
            tenencia: Include holdings data (1=yes)
            eventos: Include events data (1=yes)

        Returns:
            EvolucionDeCarteraResponse with performance metrics and history

        Raises:
            BalanzAPIError: If API call fails
        """
        if not self.auth.user_info:
            raise BalanzAPIError("User info not available")

        id_persona = self.auth.user_info.idPersona
        url = f"{self.BASE_URL}/evoluciondecartera/{id_persona}"

        params = {
            "FechaDesde": fecha_desde,
            "FechaHasta": fecha_hasta,
            "idMoneda": id_moneda,
            "Tenencia": tenencia,
            "Eventos": eventos
        }

        try:
            response = self._client.get(url, params=params, headers=self._get_headers())
            response.raise_for_status()

            return EvolucionDeCarteraResponse(**response.json())

        except httpx.HTTPError as e:
            raise BalanzAPIError(f"Failed to fetch portfolio evolution: {str(e)}")
        except Exception as e:
            raise BalanzAPIError(f"Unexpected error: {str(e)}")

    async def get_flujo_proyectado(self) -> FlujoProyectadoResponse:
        """
        Get projected bond cash flows.

        Returns:
            FlujoProyectadoResponse with bond details and projected payments

        Raises:
            BalanzAPIError: If API call fails
        """
        if not self.auth.user_info:
            raise BalanzAPIError("User info not available")

        id_persona = self.auth.user_info.idPersona
        url = f"{self.BASE_URL}/bonos/flujoproyectado/{id_persona}"

        try:
            response = self._client.get(url, headers=self._get_headers())
            response.raise_for_status()

            return FlujoProyectadoResponse(**response.json())

        except httpx.HTTPError as e:
            raise BalanzAPIError(f"Failed to fetch projected cash flow: {str(e)}")
        except Exception as e:
            raise BalanzAPIError(f"Unexpected error: {str(e)}")

    def close(self):
        """Close HTTP client."""
        self._client.close()
