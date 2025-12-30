# Product Requirements Document
## Balanz Portfolio Tracker

**Version 1.0 | December 2025**

---

## 1. Executive Summary

A desktop application for Balanz brokerage clients to visualize portfolio performance, track movements, and analyze asset distribution. The tool connects directly to the Balanz API using user credentials, with all data fetched on-demand and no local storage. This ensures simplicity, privacy, and always-current information.

---

## 2. Problem Statement

The Balanz web interface provides basic portfolio information but lacks advanced analytics, customizable views, and comprehensive performance tracking. Users who want deeper insights into their investment performance, risk metrics, or projected cash flows must resort to manual spreadsheet work or third-party tools that may not integrate well with Argentine financial instruments (LECAPs, CER bonds, CEDEARs, etc.).

---

## 3. Goals & Success Metrics

### 3.1 Primary Goals

- Provide comprehensive portfolio visualization with minimal setup
- Calculate performance metrics not available in the native interface
- Maintain a stateless architecture — no local data storage, fresh data every session
- Support distribution to other Balanz users without compromising security

### 3.2 Success Metrics

- Application loads portfolio data within 5 seconds
- All MVP features functional without requiring technical knowledge
- Zero credential persistence (credentials used only for session, never stored)

---

## 4. Available API Endpoints

The Balanz API provides the following endpoints (all require authentication token):

| Endpoint | Method | Data Provided |
|----------|--------|---------------|
| `/auth/init` | POST | Get nonce for authentication flow |
| `/auth/login` | POST | Returns AccessToken, idPersona, user info |
| `/estadodecuenta/{id}` | GET | Holdings (tenencia), liquidity, grouped by asset type, PPP, unrealized P&L |
| `/evoluciondecartera/{id}` | GET | Historical performance, daily returns, deposits/withdrawals, dividends, coupons |
| `/bonos/flujoproyectado/{id}` | GET | Projected bond cash flows, TIR, duration, coupon dates |
| `/logout` | POST | Invalidate session token |

---

## 5. MVP Features (Phase 1)

### 5.1 Authentication & Session

1. Login form with username/password (credentials held in memory only)
2. Session management with token stored in memory for API calls
3. Clean logout with token invalidation
4. Auto-logout on app close

### 5.2 Portfolio Overview Dashboard

1. Total portfolio value in ARS and USD equivalent
2. Asset allocation pie/donut chart by type (Bonos, Corporativos, Acciones, CEDEARs, Fondos)
3. Currency exposure breakdown (ARS vs USD vs USD-linked)
4. Cash/liquidity display by currency with settlement dates
5. Live MEP and CCL exchange rates (from API response)

### 5.3 Holdings Table

1. Sortable table: Ticker, Description, Quantity, Price, PPP, Value, Unrealized P&L, % Return
2. Filter by asset type
3. Color-coded P&L (green/red)
4. Portfolio weight percentage per position

### 5.4 Basic Performance View

1. Equity curve chart (portfolio value over time)
2. Date range selector (1M, 3M, 6M, YTD, 1Y, Custom)
3. Period return summary (from API's resumen data)
4. Net deposits/withdrawals distinction

### 5.5 Income & Cash Flow

1. Projected cash flow calendar from bonds (renta + amortization)
2. List view of upcoming payments with dates and amounts
3. Historical dividends and coupons received (from eventos)

---

## 6. Future Features (Phase 2+)

*Nice-to-haves for subsequent releases*

### 6.1 Advanced Performance Analytics

1. Time-Weighted Return (TWR) calculation
2. Money-Weighted Return (IRR) calculation
3. Benchmark comparison (Merval, S&P 500 via CEDEARs)
4. Monthly returns heatmap
5. CAGR calculation
6. Inflation-adjusted (real) returns using CER coefficient

### 6.2 Risk Analytics

1. Portfolio volatility (standard deviation)
2. Maximum drawdown chart with recovery periods
3. Sharpe ratio calculation
4. Concentration risk score (top N positions weight)
5. Correlation matrix between holdings

### 6.3 Bond-Specific Analytics

1. Maturity ladder visualization
2. Duration-weighted portfolio analysis
3. Yield-to-maturity aggregation
4. Projected annual income from fixed income

### 6.4 Enhanced Visualizations

1. Treemap view for hierarchical allocation
2. Performance attribution (what contributed to gains/losses)
3. Sector distribution for CEDEARs
4. Interactive charts with zoom and tooltips

### 6.5 Transaction History & Analysis

1. Full transaction log with filters
2. Realized gains/losses tracking
3. Fee/commission analysis over time
4. Cost basis tracking (FIFO/LIFO)

### 6.6 Export & Reporting

1. PDF report generation
2. CSV export for all data views


---

## 7. External Data Integration (Phase 3)

*Enrich portfolio data with external sources*

### 7.1 Yahoo Finance Integration

Leverage the free `yfinance` library to pull additional data for holdings (particularly CEDEARs).

#### Analyst Recommendations

1. Analyst ratings distribution (Strong Buy, Buy, Hold, Sell, Strong Sell)
2. Price targets (low, mean, high) vs current price
3. Number of analysts covering each stock
4. Recommendation trend over past 4 months
5. **Portfolio-weighted analyst score** — aggregate recommendation weighted by position size
6. **Upside/downside potential** — compare current prices to mean price targets

#### Fundamentals

1. P/E ratio and Forward P/E
2. EPS (trailing twelve months and forward)
3. Dividend yield (compare with your actual yield)
4. Market cap classification (mega, large, mid, small)
5. 52-week high/low with current position indicator
6. Sector and industry classification

#### News & Events

1. Recent news headlines per ticker (last 5-10 articles)
2. Earnings calendar — "3 holdings reporting next week"
3. Ex-dividend dates for upcoming dividends
4. Major corporate events (splits, spinoffs)

#### Technical Indicators

1. 50-day and 200-day moving averages
2. Price relative to moving averages (above/below signal)
3. 52-week performance comparison
4. Relative performance vs S&P 500

### 7.2 Argentine Market Data

#### BCRA API (Banco Central)

1. Official exchange rates (USD, EUR, BRL)
2. CER coefficient for inflation-adjusted return calculations
3. Monetary policy rate (LELIQ/pases) for risk-free rate comparisons
4. Historical inflation data

#### Additional Local Sources

1. Blue dollar / informal rate tracking
2. Inflation expectations (REM survey)
3. Merval index for local benchmark comparison

### 7.3 CEDEAR Ticker Mapping

CEDEARs trade under local tickers that must be mapped to their underlying US symbols for Yahoo Finance lookups.

#### Mapping Strategy

```python
CEDEAR_MAP = {
    # Balanz Ticker → Yahoo Ticker
    "AAPL": "AAPL",
    "MELI": "MELI", 
    "ASML": "ASML",
    "GOOGL": "GOOGL",
    "MSFT": "MSFT",
    "AMZN": "AMZN",
    "NVDA": "NVDA",
    "META": "META",
    # ... extend as needed
}
```

#### Mapping Sources

1. Static dictionary for common CEDEARs (covers 80% of cases)
2. BYMA (Bolsas y Mercados Argentinos) publishes official CEDEAR list
3. User override for unmapped tickers

### 7.4 Portfolio Intelligence Features

#### Aggregated Views

1. **Sector exposure treemap** — Visualize tech vs healthcare vs financials allocation
2. **Geographic exposure** — US vs Argentina vs EM breakdown
3. **Portfolio beta** — Weighted average beta of holdings
4. **Correlation matrix** — How correlated are your positions to each other

#### Calendars & Alerts

1. **Unified income calendar** — Merge Balanz bond coupons + Yahoo dividend estimates
2. **Earnings season dashboard** — Upcoming earnings for your CEDEARs
3. **Price target alerts** — Notify when holdings hit analyst targets

#### Scoring & Rankings

1. **Analyst consensus rank** — Rank holdings by analyst sentiment
2. **Valuation rank** — Rank by P/E, PEG, or other metrics
3. **Momentum rank** — Rank by recent performance

### 7.5 Data Freshness Strategy

Since there's no local storage, external data is fetched on-demand with sensible caching:

| Data Type | Fetch Frequency | Rationale |
|-----------|-----------------|-----------|
| Analyst recommendations | Once per session | Changes infrequently |
| Price targets | Once per session | Updated monthly typically |
| News headlines | On-demand per ticker | User-initiated |
| Fundamentals (P/E, EPS) | Once per session | Quarterly updates |
| CER coefficient | Once per session | Daily BCRA update |
| Moving averages | On-demand | Computed from price history |

---

## 8. Architecture Design

### 8.1 High-Level Architecture

The application follows a stateless client architecture with no persistent storage. All data is fetched fresh from the Balanz API each session.

```
┌─────────────────────────────────────────────────────────────┐
│                    DESKTOP APPLICATION                      │
│  ┌──────────────┐    ┌──────────────┐                      │
│  │   Frontend   │◄──►│   Backend    │                      │
│  │  (Web View)  │    │   (Python)   │                      │
│  └──────────────┘    └──────┬───────┘                      │
│                             │                               │
│                             ▼                               │
│                    ┌──────────────┐                        │
│                    │  API Client  │                        │
│                    │  (in-memory  │                        │
│                    │   session)   │                        │
│                    └──────┬───────┘                        │
└─────────────────────────────┼───────────────────────────────┘
                              │ HTTPS
                              ▼
                    ┌──────────────┐
                    │  Balanz API  │
                    └──────────────┘
```

### 8.2 Module Structure

```
app/
├── main.py                 # Application entry point
├── api/
│   ├── client.py          # Balanz API wrapper
│   ├── auth.py            # Authentication flow
│   └── models.py          # Pydantic response models
├── core/
│   ├── portfolio.py       # Portfolio calculations
│   ├── performance.py     # Performance metrics
│   └── cashflow.py        # Cash flow projections
├── ui/
│   ├── server.py          # FastAPI local server
│   └── static/            # Frontend assets (HTML/CSS/JS)
└── utils/                  # Helpers, config, logging
```

### 8.3 Data Flow

1. User enters credentials → held in memory only
2. App calls `/auth/init` → gets nonce → calls `/auth/login` → receives AccessToken
3. Token stored in memory (session only), used for subsequent API calls
4. Each view fetches fresh data from API on load/refresh
5. Frontend fetches data via local FastAPI endpoints
6. Charts and tables rendered client-side
7. On app close or logout, all session data discarded

### 8.4 State Management

Since there's no persistence, state is managed as follows:

| Data | Storage | Lifecycle |
|------|---------|-----------|
| Username/Password | Memory (Python variable) | Login form → auth call → discarded |
| Access Token | Memory (Python variable) | Post-login → app close |
| Portfolio Data | Memory (API response cache) | Per-request, optionally cached for current session |
| User Preferences | None | Reset each session (or use URL params) |

---

## 9. Technology Stack

### 9.1 Backend (Python)

| Component | Technology & Rationale |
|-----------|------------------------|
| HTTP Client | **httpx** – async support, connection pooling, modern API |
| Data Validation | **Pydantic** – type-safe API response parsing |
| Local API Server | **FastAPI** – lightweight, async, auto-generated OpenAPI docs |
| Data Processing | **pandas** – data manipulation, time series |

### 9.2 Frontend (pywebview + HTML/JS)

Lightweight wrapper that opens a native window with a web view. The frontend is built with standard HTML/CSS/JS.

- **Pros:** Python-only packaging, small bundle size (~15MB), familiar web tech for UI
- **Cons:** Limited native OS integration
- **Charts:** Chart.js, Plotly.js, or Apache ECharts
- **Styling:** Tailwind CSS or Bootstrap

### 9.3 Packaging & Distribution

| Tool | Description |
|------|-------------|
| **PyInstaller** | Creates standalone executables. One-file or one-folder mode. Recommended for initial distribution. |
| **Nuitka** | Compiles Python to C, better performance and obfuscation. More complex setup. |
| **GitHub Releases** | Host builds for Windows/macOS/Linux. Users download appropriate version. |

---

## 10. Security Considerations

### 10.1 Credential Handling

- Credentials entered each session — never stored on disk
- Password held in memory only during login API call, then discarded
- Access token held in memory for session duration
- All session data cleared on app close or logout

### 10.2 Network Security

- All API calls over HTTPS with certificate verification
- No third-party servers or analytics
- Local-only architecture: app → Balanz API, nothing else

### 10.3 Distribution Trust

- Open source on GitHub — users can audit code before trusting
- SHA256 checksums published with each release
- Optional code signing for trusted distribution
- Clear documentation of what data is accessed

---

## 11. Implementation Timeline

| Phase | Duration | Deliverables |
|-------|----------|--------------|
| Week 1 | Foundation | API client, auth flow, data models, basic FastAPI server |
| Week 2 | Core UI | Dashboard, holdings table, allocation charts |
| Week 3 | Performance & Polish | Equity curve, cash flow view, packaging, testing |
| Phase 2 | Ongoing | Advanced analytics, risk metrics, export features |
| Phase 3 | Ongoing | Yahoo Finance integration, CEDEAR mapping, analyst data, sector analysis |

---

## Appendix: Key Dependencies

```txt
# requirements.txt
httpx>=0.25.0
fastapi>=0.104.0
uvicorn>=0.24.0
pydantic>=2.5.0
pandas>=2.1.0
pywebview>=4.4.0
yfinance>=0.2.0          # Phase 3: Yahoo Finance data
pyinstaller>=6.0.0       # dev dependency
```

---

## Appendix: API Response Examples

### Estado de Cuenta (Holdings)

Key fields from `/estadodecuenta/{id}`:

```python
{
    "tenenciaAgrupada": [...],  # Holdings grouped by type with totals
    "tenencia": [               # Individual positions
        {
            "Ticker": "AL35",
            "Cantidad": 100,
            "Precio": 1145.6,
            "PPP": 826.8,           # Purchase price average
            "ValorActual": 114560,
            "NoRealizado": 31880,   # Unrealized P&L
            "PorcRendimiento": 38.56,
            "PorcTenencia": 0.26,   # Portfolio weight %
        }
    ],
    "liquidez": [...],          # Cash by currency
    "tenenciaActual": [{
        "CotizacionMEP": 1485.88,
        "CotizacionCCL": 1527.17,
    }]
}
```

### Evolución de Cartera (Performance)

Key fields from `/evoluciondecartera/{id}`:

```python
{
    "resumen": [...],      # Summary by period (1M, 3M, YTD, etc.)
    "rendimiento": [       # Daily returns
        {"Fecha": "29/09/2025", "Rendimiento": -3.1, "RendimientoAbs": -1.72}
    ],
    "tenencia": [...],     # Daily portfolio value
    "eventos": [           # Transactions, dividends, coupons
        {"date": "19/12/2025", "type": "arrowUp", "text": "D", "description": "+$1017477"}
    ]
}
```

### Flujo Proyectado (Cash Flows)

Key fields from `/bonos/flujoproyectado/{id}`:

```python
{
    "tabla": [...],        # Bond details (TIR, duration, next payment)
    "flujo": [             # Projected payments
        {
            "codigoespeciebono": "AL35",
            "fecha": "2026-01-09",
            "renta": 2.063,
            "amort": 0,
            "total": 2.063,
            "tipo_moneda": 2  # 2 = USD
        }
    ]
}
```