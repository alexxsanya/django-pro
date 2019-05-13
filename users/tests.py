from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.

class TestUserSignUpApi(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = {
            'fullname':'Alex Ssanya',
            'email': 'alex@gmail.com',
            'password': 'Password'
        }
    
    def test_signup_api_exists(self):
        url = reverse('users:signup_users')
        response = self.client.get(url, self.user)
        self.assertContains(response,'Alex Ssanya')

