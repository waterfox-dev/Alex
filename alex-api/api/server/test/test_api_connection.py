from server.models import User

from rest_framework.test import APITestCase


class TestApiConnection(APITestCase):
    
    def setUp(self) -> None:
        User.objects.all().delete()

        self.user = User(
            username='testuser', 
            email='testuser@gmail.com',
            password='12345', 
            first_name='Test',
            last_name='User'
        ).save()
        
    def test_connection(self):
        response = self.client.post('http://127.0.0.1:8000/api/users/check_password/', {'mail': 'testuser@gmail.com', 'password': '12345'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['exists']['email'], 'testuser@gmail.com')
        
    def test_connection_fail(self):
        response = self.client.post('http://127.0.0.1:8000/api/users/check_password/', {'mail': 'testuser@gmail.com', 'password': '1234'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['exists'], False)
        
    def test_connection_fail_no_mail(self):
        response = self.client.post('http://127.0.0.1:8000/api/users/check_password/', {'password': '12345'})
        self.assertEqual(response.status_code, 400)
    
    def test_connection_fail_no_password(self):
        response = self.client.post('http://127.0.0.1:8000/api/users/check_password/', {'mail': 'testuser@gmail.com'})
        self.assertEqual(response.status_code, 400)