# Balanz Portfolio Tracker

A desktop application for Balanz brokerage clients to visualize portfolio performance, track movements, and analyze asset distribution.

## Features (MVP - Phase 1)

### ✅ Implemented
- **Authentication & Session Management**
  - Secure login with Balanz credentials
  - In-memory session storage (no data persisted to disk)
  - Clean logout with token invalidation
  - Auto-logout on app close

### 🚧 Coming Soon
- Portfolio Overview Dashboard
- Holdings Table with filters
- Performance Analytics
- Income & Cash Flow Projections

## Security

- **Zero credential persistence**: Your username and password are used only for authentication and never stored
- **In-memory sessions**: Access tokens are held in memory only during the session
- **HTTPS only**: All API calls use secure HTTPS connections
- **No analytics or tracking**: Your data never leaves your machine except to communicate with Balanz API

## Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package installer)

### Setup

1. Clone this repository:
```bash
cd "Balanz Portfolio Tracker"
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

From the project root directory:

```bash
python app/main.py
```

The application will:
1. Start a local FastAPI server on port 8765
2. Open a desktop window with the application interface
3. Wait for you to login with your Balanz credentials

## Usage

1. **Login**: Enter your Balanz username and password
2. **Dashboard**: View your portfolio (coming soon)
3. **Logout**: Click "Cerrar Sesión" to logout and clear all session data

## Architecture

```
app/
├── main.py                 # Application entry point
├── api/
│   ├── client.py          # Balanz API wrapper
│   ├── auth.py            # Authentication flow
│   └── models.py          # Pydantic response models
├── core/                   # Business logic (coming soon)
├── ui/
│   ├── server.py          # FastAPI local server
│   └── static/            # Frontend assets (HTML/CSS/JS)
└── utils/                  # Helpers and utilities
```

## Data Flow

1. User enters credentials → held in memory only
2. App calls Balanz `/auth/init` → gets nonce
3. App calls `/auth/login` → receives AccessToken
4. Token stored in memory for API calls
5. On logout or app close → all session data discarded

## Technology Stack

- **Backend**: Python with FastAPI
- **HTTP Client**: httpx (async support)
- **Data Validation**: Pydantic
- **Desktop UI**: pywebview (native window wrapper)
- **Frontend**: HTML/CSS/JavaScript

## Development

### Project Structure

The application follows a modular architecture with clear separation of concerns:

- `api/`: Handles all communication with Balanz API
- `core/`: Business logic for portfolio calculations
- `ui/`: FastAPI server and frontend assets
- `utils/`: Shared utilities and helpers

### API Endpoints

The local FastAPI server provides these endpoints:

- `POST /api/login` - Authenticate with Balanz
- `POST /api/logout` - Logout and clear session
- `GET /api/status` - Check authentication status
- `GET /api/portfolio` - Get portfolio holdings (requires auth)
- `GET /api/performance` - Get performance data (requires auth)
- `GET /api/cashflow` - Get projected cash flows (requires auth)

## Roadmap

### Phase 1 (Current - MVP)
- ✅ Authentication & Session
- 🚧 Portfolio Overview Dashboard
- 🚧 Holdings Table
- 🚧 Basic Performance View
- 🚧 Cash Flow Calendar

### Phase 2
- Advanced Performance Analytics (TWR, IRR, CAGR)
- Risk Analytics (volatility, Sharpe ratio, drawdown)
- Bond-Specific Analytics (duration, yield curve)
- Enhanced Visualizations

### Phase 3
- Yahoo Finance Integration (analyst ratings, fundamentals)
- BCRA API Integration (CER, inflation data)
- CEDEAR analysis with US market data
- Portfolio intelligence features

## Contributing

This is a personal project for Balanz clients. If you find bugs or have suggestions, please open an issue.

## License

This project is provided as-is for personal use. Not affiliated with or endorsed by Balanz.

## Disclaimer

This application is an unofficial tool and is not affiliated with, endorsed by, or connected to Balanz in any way. Use at your own risk. The developers are not responsible for any issues arising from the use of this application.

Always verify important financial information directly with the official Balanz platform.
