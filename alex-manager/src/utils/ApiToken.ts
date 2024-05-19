class ApiToken {
    public static token: string;
    public static refresh: string;
    private static expiration: Date; 
    public static username: string;
    public static password: string;
    public static TOKEN_URL = "http://localhost:8000/api/token";
    public static REFRESH_URL = "http://localhost:8000/api/token/refresh";

    public static setToken(token: string, expiration: Date): void {
        ApiToken.token = token;
        ApiToken.expiration = expiration;
        localStorage.setItem('token', token);
    }

    public static async refreshToken(): Promise<void> {
        try {
            const response = await fetch(ApiToken.refresh ? ApiToken.REFRESH_URL : ApiToken.TOKEN_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(ApiToken.refresh ? { refresh: ApiToken.refresh } : { username: ApiToken.username, password: ApiToken.password }),
            });

            if (!response.ok) {
                throw new Error('Failed to refresh token');
            }

            const data = await response.json();
            ApiToken.setToken(data.access, new Date(Date.now() + 1000 * 60 * 20));
            if (data.refresh) {
                ApiToken.refresh = data.refresh;
            }
        } catch (error) {
            console.error('Error:', error);
        }
    }

    public static async getToken(): Promise<string> {
        if (!ApiToken.token || !ApiToken.expiration || ApiToken.expiration < new Date()) {
            await ApiToken.refreshToken();
        }
        return ApiToken.token;
    }

    public static setCreds(username: string, password: string): void {
        ApiToken.username = username;
        ApiToken.password = password;
    }

    public static isLogged(): boolean {
        return !!ApiToken.token && ApiToken.expiration > new Date();
    }
}

export default ApiToken;
