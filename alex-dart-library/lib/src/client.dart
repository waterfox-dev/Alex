class Client{

  static String baseUrl = ""; 
  static Client? _instance;

  static Client getInstance(){
    _instance ??= Client();
    return Client();
  }
}