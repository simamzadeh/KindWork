from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages


class AxesLockoutTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.login_url = reverse('login')

    def test_lockout_after_failed_attempts(self):
        # Try to login with wrong password multiple times
        for i in range(5):
            response = self.client.post(self.login_url, {
                'username': 'testuser',
                'password': 'wrongpassword'
            })
            self.assertEqual(response.status_code, 200)

        # Next attempt should redirect to lockout page
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertRedirects(response, '/locked/')

    def test_successful_login_resets_failed_attempts(self):
        # Try to login with wrong password a few times
        for i in range(3):
            response = self.client.post(self.login_url, {
                'username': 'testuser',
                'password': 'wrongpassword'
            })
            self.assertEqual(response.status_code, 200)

        # Now login successfully
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'password'
        })
        self.assertRedirects(response, '/')

        # Failed attempts should be reset, so we can try wrong passwords again
        for i in range(3):
            response = self.client.post(self.login_url, {
                'username': 'testuser',
                'password': 'wrongpassword'
            })
            self.assertEqual(response.status_code, 200)