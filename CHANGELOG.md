# Changelog

All notable changes to the Balanz Portfolio Tracker will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Portfolio Overview Dashboard (in progress)
- Holdings Table (in progress)
- Performance Analytics (in progress)
- Cash Flow Calendar (in progress)

## [0.1.0] - TBD

### Added
- Initial release
- Authentication & session management
  - Secure login with Balanz credentials
  - In-memory session storage (no disk persistence)
  - Clean logout with token invalidation
  - Auto-logout on app close
- Backend API client
  - Complete Balanz API integration
  - Pydantic models for all API responses
  - Async HTTP client with connection pooling
- FastAPI local server
  - Authentication endpoints
  - Portfolio data endpoints (ready for frontend)
  - Static file serving
  - CORS middleware
- Desktop application
  - pywebview native window wrapper
  - Responsive login screen
  - Dashboard layout (placeholder)
  - Clean, modern UI design
- Distribution & packaging
  - PyInstaller configuration for all platforms
  - Build scripts for macOS, Windows, and Linux
  - DMG creation for macOS
  - GitHub Actions workflow for automated releases
  - Comprehensive distribution documentation
- Documentation
  - README with installation and usage instructions
  - PRD (Product Requirements Document)
  - API documentation
  - Implementation status tracking
  - Distribution guide
  - Quickstart guide

### Security
- Zero credential persistence
- HTTPS-only API communication
- In-memory session management
- No third-party analytics or tracking
- Local-only architecture

### Platform Support
- macOS 10.13 (High Sierra) and later
- Windows 10 and later
- Linux (Ubuntu 18.04+, other distributions with GTK 3.0+)

### Known Issues
- Dashboard features are placeholders (coming in next release)
- No session timeout handling
- Async/sync mixing in auth methods needs refactoring

---

## Version History

- **0.1.0** - Initial MVP release with authentication and packaging infrastructure
- Future versions will add portfolio visualization, analytics, and external data integration

---

## Release Notes Format

Each release includes:
- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Features to be removed in future releases
- **Removed**: Features removed in this release
- **Fixed**: Bug fixes
- **Security**: Security improvements or fixes
