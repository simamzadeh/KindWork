from django.test import TestCase, override_settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

@override_settings(AXES_ENABLED=False)
class RegistrationViewTestCase(TestCase):

    def setUp(self):
        # Valid user data for a new registration
        self.valid_user_data = {
            'username': 'newuser',
            'password1': 'strongpassword',
            'password2': 'strongpassword',
            'email': 'newuser@example.com',
        }
        
        # Invalid user data for testing error messages
        self.invalid_user_data = {
            'username': 'existinguser',  # Duplicate username for testing
            'password1': 'strongpassword',
            'password2': 'differentpassword',  # Passwords do not match
            'email': 'newuser@example.com',
        }
        
        # Create an existing user to test against
        User.objects.create_user(username='existinguser', password='strongpassword', email='existing@example.com')

    def test_registration_success(self):
        # Test successful registration
        response = self.client.post(reverse('register'), data=self.valid_user_data)

        # Check that a new user has been created
        self.assertEqual(User.objects.count(), 2)  # 1 existing user + 1 new user
        
        # Ensure the response was a redirect
        self.assertEqual(response.status_code, 302)  # Redirect status

        # Check for successful registration message in the session
        messages = list(get_messages(response.wsgi_request))
        self.assertIn("Registration successful.", [m.message for m in messages])

    def test_registration_failure(self):
        # Test unsuccessful registration due to duplicate username and password mismatch
        response = self.client.post(reverse('register'), data=self.invalid_user_data)

        # Check that a new user has not been created
        self.assertEqual(User.objects.count(), 1)  # Still only the original user

        # Ensure the response is a 200 (not redirected) and the form is rendered again
        self.assertEqual(response.status_code, 200)  # Expected status code for rendering the form
        self.assertTemplateUsed(response, 'register.html')  # Ensure it renders the register template
        
        # Check if the error message is included in the response
        messages = list(get_messages(response.wsgi_request))
        self.assertIn("Unsuccessful registration. Invalid information.", [m.message for m in messages])

        # Verify that the form contains errors
        form = response.context['register_form']
        self.assertTrue(form.errors)  # Ensure there are form errors
        self.assertIn('username', form.errors)  # Check for username error
        self.assertIn('password2', form.errors)  # Check for password mismatch error
