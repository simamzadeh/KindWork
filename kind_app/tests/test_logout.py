from django.test import TestCase, override_settings
from django.urls import reverse
from django.contrib.auth.models import User


@override_settings(AXES_ENABLED=False)
class LogoutViewTestCase(TestCase):

    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_logout_user(self):
        # Test that the user can log out successfully
        response = self.client.get(reverse('logout'))  # Adjust if your URL pattern is different

        # Ensure the response is successful and renders the logout template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logout.html')

        # Check that the logout message is in the response
        self.assertContains(response, "You have been logged out successfully.")

        # Ensure the user is logged out
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_user_is_logged_out(self):
        # Test that the user is logged out after the logout request
        self.client.get(reverse('logout'))  # Perform the logout

        # Attempt to access a protected view to verify logout (for example, check the current authentication status)
        response = self.client.get(reverse('check-auth'))  # Adjust this URL as needed

        # Check that the user is no longer authenticated
        self.assertEqual(response.json()['isAuthenticated'], False)

    def test_logout_message_displayed(self):
        # Test that the logout message is displayed correctly
        response = self.client.get(reverse('logout'))  # Log out
        messages = list(response.wsgi_request._messages)

        # Check if the expected logout message is in the messages list
        self.assertEqual(len(messages), 0)  # Since logout does not set a message

        # Check the message content
        self.assertContains(response, "You have been logged out successfully.")
