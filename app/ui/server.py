"""FastAPI local server for the desktop application."""
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
from typing import Optional
import asyncio

from ..api.auth import BalanzAuth, AuthenticationError
from ..api.client import BalanzClient, BalanzAPIError


# Request/Response models
class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    success: bool
    message: str
    user_name: Optional[str] = None
    user_id: Optional[str] = None


class LogoutResponse(BaseModel):
    success: bool
    message: str


class StatusResponse(BaseModel):
    authenticated: bool
    user_name: Optional[str] = None


# Initialize FastAPI app
app = FastAPI(title="Balanz Portfolio Tracker API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global auth and client instances (in-memory session)
auth_instance: Optional[BalanzAuth] = None
client_instance: Optional[BalanzClient] = None


def get_auth() -> BalanzAuth:
    """Get or create auth instance."""
    global auth_instance
    if auth_instance is None:
        auth_instance = BalanzAuth()
    return auth_instance


def get_client() -> BalanzClient:
    """Get or create client instance."""
    global client_instance, auth_instance
    if client_instance is None:
        if auth_instance is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        client_instance = BalanzClient(auth_instance)
    return client_instance


def cleanup_session():
    """Clean up session data from memory."""
    global auth_instance, client_instance
    if client_instance:
        client_instance.close()
        client_instance = None
    if auth_instance:
        auth_instance.close()
        auth_instance = None


# Static files
static_dir = Path(__file__).parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main application page."""
    index_path = Path(__file__).parent / "static" / "index.html"
    if index_path.exists():
        return FileResponse(index_path)
    else:
        # Fallback if index.html doesn't exist yet
        return HTMLResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Balanz Portfolio Tracker</title>
        </head>
        <body>
            <h1>Balanz Portfolio Tracker</h1>
            <p>Frontend files not found. Please create static/index.html</p>
        </body>
        </html>
        """)


@app.post("/api/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    """
    Authenticate user with Balanz API.
    Credentials are held in memory only during this request.
    """
    try:
        auth = get_auth()

        # Step 1: Initialize auth flow to get nonce
        nonce = await auth.init(request.username)

        # Step 2: Login with credentials
        user_info = await auth.login(request.username, request.password, nonce)

        # Password is now out of scope and will be garbage collected
        return LoginResponse(
            success=True,
            message="Login successful",
            user_name=user_info.Nombre,
            user_id=user_info.idPersona
        )

    except AuthenticationError as e:
        raise HTTPException(status_code=401, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@app.post("/api/logout", response_model=LogoutResponse)
async def logout():
    """
    Logout and clear session data from memory.
    """
    try:
        auth = get_auth()
        await auth.logout()
        cleanup_session()

        return LogoutResponse(
            success=True,
            message="Logged out successfully"
        )

    except Exception as e:
        # Even if logout fails, cleanup session
        cleanup_session()
        raise HTTPException(status_code=500, detail=f"Logout error: {str(e)}")


@app.get("/api/status", response_model=StatusResponse)
async def status():
    """
    Check authentication status.
    """
    try:
        auth = get_auth()
        user_info = auth.get_user_info()

        return StatusResponse(
            authenticated=auth.is_authenticated(),
            user_name=user_info.Nombre if user_info else None
        )

    except Exception:
        return StatusResponse(authenticated=False)


@app.get("/api/portfolio")
async def get_portfolio(fecha: Optional[str] = None):
    """
    Get current portfolio holdings and allocation.
    """
    try:
        client = get_client()
        data = await client.get_estado_de_cuenta(fecha=fecha)
        return data.model_dump()

    except BalanzAPIError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@app.get("/api/performance")
async def get_performance(
    fecha_desde: str,
    fecha_hasta: str,
    id_moneda: int = 2
):
    """
    Get portfolio performance over time.
    """
    try:
        client = get_client()
        data = await client.get_evolucion_de_cartera(
            fecha_desde=fecha_desde,
            fecha_hasta=fecha_hasta,
            id_moneda=id_moneda
        )
        return data.model_dump()

    except BalanzAPIError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@app.get("/api/cashflow")
async def get_cashflow():
    """
    Get projected bond cash flows.
    """
    try:
        client = get_client()
        data = await client.get_flujo_proyectado()
        return data.model_dump()

    except BalanzAPIError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on app shutdown."""
    cleanup_session()
