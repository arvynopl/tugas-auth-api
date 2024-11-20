// File app/static/js/auth.js

const API_BASE_URL = 'http://127.0.0.1:8000/api/v1';

class Auth {
    static async login(apiKey) {
        try {
            const response = await fetch(`${API_BASE_URL}/secure`, {
                method: 'GET',
                headers: {
                    'X-API-Key': apiKey
                }
            });

            const data = await response.json();
            
            if (response.ok) {
                localStorage.setItem('apiKey', apiKey);
                return { success: true, data };
            } else {
                throw new Error(data.detail || 'Login failed');
            }
        } catch (error) {
            return { success: false, error: error.message };
        }
    }

    static logout() {
        localStorage.removeItem('apiKey');
        window.location.href = '/login';
    }

    static isAuthenticated() {
        return !!localStorage.getItem('apiKey');
    }

    static getApiKey() {
        return localStorage.getItem('apiKey');
    }

    static async validateSession() {
        const apiKey = this.getApiKey();
        if (!apiKey) {
            return false;
        }

        try {
            const response = await fetch(`${API_BASE_URL}/secure`, {
                headers: {
                    'X-API-Key': apiKey
                }
            });
            return response.ok;
        } catch {
            return false;
        }
    }
}