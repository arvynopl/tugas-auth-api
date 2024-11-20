// File app/static/js/dashboard.js

class Dashboard {
    static async initialize() {
        if (!Auth.isAuthenticated()) {
            window.location.href = '/login';
            return;
        }

        await this.loadUserData();
    }

    static async loadUserData() {
        try {
            const response = await fetch(`${API_BASE_URL}/secure`, {
                headers: {
                    'X-API-Key': Auth.getApiKey()
                }
            });

            if (!response.ok) {
                throw new Error('Failed to fetch user data');
            }

            const data = await response.json();
            this.updateUI(data);
        } catch (error) {
            console.error('Error:', error);
            Auth.logout();
        }
    }

    static updateUI(data) {
        document.getElementById('userData').innerHTML = `
            <p class="text-gray-800">Client: <span class="font-semibold">${data.client}</span></p>
            <p class="text-gray-600 mt-2">${data.message}</p>
        `;
    }
}