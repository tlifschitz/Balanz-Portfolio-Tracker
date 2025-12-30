# Quick Start Guide

Get up and running with Balanz Portfolio Tracker in 5 minutes.

---

## Prerequisites

- Python 3.9 or higher
- Balanz account credentials
- macOS, Linux, or Windows

---

## Installation (One Command)

```bash
./setup.sh
```

This will:
1. Create a virtual environment
2. Install all dependencies
3. Set up the project

---

## Running the Application

### Option 1: Using the run script (macOS/Linux)
```bash
./run.sh
```

### Option 2: Manual run
```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Run the app
python app/main.py
```

---

## First Time Usage

1. **Launch the app** using one of the methods above
2. **Wait for the window to open** (takes 1-2 seconds)
3. **Enter your credentials**:
   - Username: Your Balanz username
   - Password: Your Balanz password
4. **Click "Iniciar Sesión"**
5. **You're in!** The dashboard will appear

---

## What You Can Do (MVP Status)

### ✅ Available Now
- Secure login/logout
- Session management
- View welcome screen

### 🚧 Coming Soon
- Portfolio overview with charts
- Holdings table with filters
- Performance analytics
- Cash flow projections

---

## Troubleshooting

### Port already in use
If you see an error about port 8765 being in use:
```bash
# Find and kill the process using port 8765
lsof -ti:8765 | xargs kill -9
```

### Dependencies not installing
Make sure you have Python 3.9+:
```bash
python3 --version
```

If using an older version, upgrade Python first.

### Login fails
- Check your Balanz credentials
- Make sure you have internet connection
- Verify the Balanz API is accessible

### Window doesn't open
On macOS, you may need to install pywebview dependencies:
```bash
# macOS only
pip install pyobjc-framework-WebKit
```

On Linux:
```bash
# Ubuntu/Debian
sudo apt-get install python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-webkit2-4.0
```

---

## Security Notes

- Your credentials are **never stored** on disk
- Password is used only for authentication and immediately discarded
- Access token is held in memory during the session
- All data is cleared when you logout or close the app
- Only communicates with Balanz API (no third-party servers)

---

## Next Steps

After successfully running the app:

1. **Check [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md)** to see what's implemented
2. **Read [README.md](README.md)** for detailed documentation
3. **Review [PRD.md](PRD.md)** to see the full roadmap

---

## Need Help?

- **Issues**: Create an issue in the repository
- **Documentation**: See README.md and PRD.md
- **Architecture**: Check IMPLEMENTATION_STATUS.md

---

## Development

To contribute or extend the app:

```bash
# Install dev dependencies
pip install pytest black flake8

# Run in development mode
python app/main.py

# The FastAPI server will be at: http://127.0.0.1:8765
```

---

**Enjoy tracking your Balanz portfolio!**
