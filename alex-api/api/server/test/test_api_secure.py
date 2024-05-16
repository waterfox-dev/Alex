from django.contrib.auth.models import User

from rest_framework.test import APITestCase




class TestLoanBookApi(APITestCase):
    
    secure_route = "http://127.0.0.1:8000/api/authors/"    

    def test_post_forbiden(self):
        response = self.client.post(self.secure_route, {"name": "Test", "first_name": "Test"})
        self.assertEqual(response.status_code, 401)
            
    def test_get_authorized(self):
        response = self.client.get(self.secure_route)
        self.assertEqual(response.status_code, 200)
            
    def test_post_authorized(self): 
        User.objects.create_superuser("root", "root", "root") 
        token = self.client.post("http://127.0.0.1:8000/api/token", {"username": "root", "password": "root"}).json()
        response = self.client.post(
            self.secure_route, 
            HTTP_AUTHORIZATION=f"Bearer {token['access']}", 
            data={""}
        )
        
        self.assertEqual(response.status_code, 201)
            