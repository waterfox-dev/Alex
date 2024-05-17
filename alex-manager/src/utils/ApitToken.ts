class ApiToken {
    public static token: string;
    public static refresh: String;

    private static expiration: Date; 

    public static username: string;
    public static password: string;

    public static TOKEN_URL = "http://localhost:8000/api/token"
    public static REFRESH_URL = "http://localhost:8000/api/token/refresh"

    public static setToken(token: string, expiration: Date): void {
        ApiToken.token = token;
        ApiToken.expiration = expiration;

    } 

    public static refreshToken(): void{
        if(ApiToken.refresh){   
            fetch(ApiToken.REFRESH_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({refresh: ApiToken.refresh})
            })
            .then(response => response.json())
            .then(data => {
                ApiToken.setToken(data.access, new Date(Date.now() + 1000*60*20));
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }else{
            fetch(ApiToken.TOKEN_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({username: ApiToken.username, password: ApiToken.password})
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                ApiToken.setToken(data.access, new Date(Date.now() + 1000*60*20));
                ApiToken.refresh = data.refresh;
            })
        }
    }    

    public static getToken(): string {
        if (ApiToken.expiration < new Date()) {
            ApiToken.refreshToken();
            return ApiToken.token;
        }
        else if (!ApiToken.token || !ApiToken.expiration)  {
            ApiToken.refreshToken();
            return ApiToken.token;
        }
        return ApiToken.token;
    }

    public static setCreds(username: string, password: string): void {
        ApiToken.username = username;
        ApiToken.password = password;
    }
}

export default ApiToken;