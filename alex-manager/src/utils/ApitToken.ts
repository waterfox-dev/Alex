class ApiToken {
    private static token: string;
    private static refresh: String;

    private static expiration: Date; 

    public static TOKEN_URL = "http://localhost:8000/api/token/"
    public static REFRESH_URL = "http://localhost:8000/api/token/refresh/"

    public static setToken(token: string, expiration: Date): void {
        this.token = token;
        this.expiration = expiration;
    } 

    public static refreshToken(): void{
        if(this.refresh){   
            fetch(this.REFRESH_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({refresh: this.refresh})
            })
            .then(response => response.json())
            .then(data => {
                this.setToken(data.access, new Date(Date.now() + 1000*60*20));
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }else{
            //TODO: redirect to login
        }
    }    

    public static getToken(): string {
        if (this.expiration < new Date()) {
            this.refreshToken();
        }
        return ApiToken.token;
    }
}

export default ApiToken;