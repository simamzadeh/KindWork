from django.test import TestCase, override_settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Disable axes for login tests
@override_settings(AXES_ENABLED=False)
class LoginViewTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_login_page_renders(self):
        # Test that the login page renders correctly
        response = self.client.get(reverse('login'))  # Adjust this if your URL pattern is different
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Login')  # Check if the page contains the word 'Login'
        self.assertIsInstance(response.context['login_form'], AuthenticationForm)

    def test_login_with_valid_credentials(self):
        # Test login with valid credentials
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password'
        })

        # Ensure redirection occurs after successful login
        self.assertRedirects(response, '/')

        # Check that the user is logged in
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_with_invalid_credentials(self):
        # Test login with invalid credentials
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })

        # Ensure the page reloads with error message
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        # Check if the error message exists in the messages
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), "Invalid username or password.")

        # Check that the user is not logged in
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_login_with_empty_fields(self):
        # Test login with empty fields
        response = self.client.post(reverse('login'), {
            'username': '',
            'password': ''
        })

        # Ensure the page reloads with error message
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        # Check if the error message exists in the messages
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), "Invalid username or password.")

        # Check that the user is not logged in
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_login_with_invalid_form(self):
        # Test login with invalid form input
        response = self.client.post(reverse('login'), {
            'username': 'invaliduser',
            'password': 'invalidpassword'
        })

        # Ensure the page reloads with error message
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        # Check if the error message exists in the messages
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), "Invalid username or password.")

        # Check that the user is not logged in
        self.assertFalse(response.wsgi_request.user.is_authenticated)
