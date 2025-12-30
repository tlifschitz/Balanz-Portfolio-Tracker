"""
Balanz Portfolio Tracker - Main Application Entry Point

This desktop application provides portfolio visualization and analytics for Balanz clients.
All data is fetched on-demand from the Balanz API with no local storage.
"""
import webview
import uvicorn
import threading
import sys
from pathlib import Path

# Add app directory to Python path
app_dir = Path(__file__).parent
sys.path.insert(0, str(app_dir.parent))

from app.ui.server import app as fastapi_app


class BalanzPortfolioTracker:
    """Main application class."""

    def __init__(self):
        self.server_thread = None
        self.server_port = 8765

    def start_server(self):
        """Start FastAPI server in a background thread."""
        config = uvicorn.Config(
            fastapi_app,
            host="127.0.0.1",
            port=self.server_port,
            log_level="warning"
        )
        server = uvicorn.Server(config)
        server.run()

    def run(self):
        """Start the application."""
        # Start FastAPI server in background thread
        self.server_thread = threading.Thread(target=self.start_server, daemon=True)
        self.server_thread.start()

        # Wait for server to start
        import time
        time.sleep(1)

        # Create and start pywebview window
        window = webview.create_window(
            title="Balanz Portfolio Tracker",
            url=f"http://127.0.0.1:{self.server_port}",
            width=1280,
            height=800,
            resizable=True,
            min_size=(800, 600)
        )

        # Start webview (blocks until window is closed)
        webview.start()

        print("Application closed. Cleaning up...")


def main():
    """Application entry point."""
    print("Starting Balanz Portfolio Tracker...")
    print("=" * 50)
    print("SECURITY NOTE:")
    print("- Credentials are used only for authentication")
    print("- Never stored on disk")
    print("- All session data cleared on app close")
    print("=" * 50)

    app = BalanzPortfolioTracker()
    app.run()


if __name__ == "__main__":
    main()
