from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class LoginLogoutTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test',
                                             email="test@example.com",
                                             password="Test@123")
        self.url = "account:"

    def test_login(self):
        data = {
            "username": "test",
            "password": "Test@123"
        }
        response = self.client.post(reverse(self.url + "login"), data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('home:index'))

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse(self.url + "logout"))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse(self.url + "login"))
