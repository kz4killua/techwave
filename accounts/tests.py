from django.test import TestCase
from django.urls import reverse
from accounts.models import User

class LoginTestCase(TestCase):

    def setUp(self):
        """Create a test user."""
        self.username = "test_user"
        self.password = "test_password"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.login_url = reverse('accounts:login')

    def test_valid_login(self):
        """Test valid login with correct username and password."""
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue('_auth_user_id' in self.client.session)


    def test_invalid_login(self):
        """Test invalid login with incorrect username or password."""
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password.')
        self.assertFalse('_auth_user_id' in self.client.session)
