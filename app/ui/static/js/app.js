/**
 * Balanz Portfolio Tracker - Frontend Application
 */

// Application state
const state = {
    authenticated: false,
    userName: null
};

// DOM Elements
const loginScreen = document.getElementById('login-screen');
const dashboardScreen = document.getElementById('dashboard-screen');
const loginForm = document.getElementById('login-form');
const loginBtn = document.getElementById('login-btn');
const logoutBtn = document.getElementById('logout-btn');
const errorMessage = document.getElementById('error-message');
const userNameDisplay = document.getElementById('user-name');

// Utility Functions
function showScreen(screen) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    screen.classList.add('active');
}

function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove('hidden');
}

function hideError() {
    errorMessage.classList.add('hidden');
}

function setLoading(isLoading) {
    const btnText = loginBtn.querySelector('.btn-text');
    const btnLoader = loginBtn.querySelector('.btn-loader');

    loginBtn.disabled = isLoading;

    if (isLoading) {
        btnText.classList.add('hidden');
        btnLoader.classList.remove('hidden');
    } else {
        btnText.classList.remove('hidden');
        btnLoader.classList.add('hidden');
    }
}

// API Functions
async function checkAuthStatus() {
    try {
        const response = await fetch('/api/status');
        const data = await response.json();

        if (data.authenticated) {
            state.authenticated = true;
            state.userName = data.user_name;
            updateUIAfterLogin();
        } else {
            state.authenticated = false;
            state.userName = null;
            showScreen(loginScreen);
        }
    } catch (error) {
        console.error('Error checking auth status:', error);
        showScreen(loginScreen);
    }
}

async function handleLogin(event) {
    event.preventDefault();
    hideError();
    setLoading(true);

    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value;

    if (!username || !password) {
        showError('Por favor ingresa usuario y contraseña');
        setLoading(false);
        return;
    }

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok && data.success) {
            state.authenticated = true;
            state.userName = data.user_name;

            // Clear form
            loginForm.reset();

            // Update UI
            updateUIAfterLogin();
        } else {
            showError(data.detail || 'Error al iniciar sesión. Verifica tus credenciales.');
        }
    } catch (error) {
        console.error('Login error:', error);
        showError('Error de conexión. Por favor intenta nuevamente.');
    } finally {
        setLoading(false);
    }
}

async function handleLogout() {
    try {
        const response = await fetch('/api/logout', {
            method: 'POST'
        });

        if (response.ok) {
            state.authenticated = false;
            state.userName = null;
            showScreen(loginScreen);
        } else {
            alert('Error al cerrar sesión');
        }
    } catch (error) {
        console.error('Logout error:', error);
        alert('Error de conexión al cerrar sesión');
    }
}

function updateUIAfterLogin() {
    userNameDisplay.textContent = state.userName || 'Usuario';
    showScreen(dashboardScreen);
}

// Event Listeners
loginForm.addEventListener('submit', handleLogin);
logoutBtn.addEventListener('click', handleLogout);

// Initialize app
async function init() {
    console.log('Initializing Balanz Portfolio Tracker...');
    await checkAuthStatus();
}

// Start the application
init();
