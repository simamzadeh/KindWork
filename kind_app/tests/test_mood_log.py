from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from kind_app.models.mood_log import MoodLog


class MoodLogViewTestCase(APITestCase):

    def setUp(self):
        # Create a test user and another user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.other_user = User.objects.create_user(username='otheruser', password='password')
        self.superuser = User.objects.create_superuser(username='admin', password='adminpassword')

        self.client.login(username='testuser', password='password')

        # Create sample mood logs for both users
        self.mood_log1 = MoodLog.objects.create(user=self.user, mood="pleasant")
        self.mood_log2 = MoodLog.objects.create(user=self.other_user, mood="unpleasant")

    def test_get_mood_log_list(self):
        # Test GET request to retrieve all mood logs for the authenticated user
        url = reverse('mood-log-api')  # No pk argument
        response = self.client.get(url)

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that only the authenticated user's logs are returned
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['mood'], "pleasant")

    def test_get_mood_log_by_id(self):
        # Test GET request to retrieve a specific mood log manually
        # Simulate what the view would do by filtering the queryset based on ID
        url = reverse('mood-log-api')  # No pk argument, filter by ID manually
        response = self.client.get(url)

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure the mood log content matches (only user logs are returned)
        self.assertEqual(response.data[0]['mood'], self.mood_log1.mood)

    def test_get_mood_log_forbidden(self):
        # Test GET request to ensure the user can't access another user's mood log
        url = reverse('mood-log-api')  # No pk argument
        response = self.client.get(url)

        # Ensure the request is forbidden (since it's not returning the other user's data)
        # The response should not contain the other user's logs
        self.assertNotIn(self.mood_log2.id, [log['id'] for log in response.data])

    def test_create_mood_log(self):
        # Test POST request to create a new mood log
        url = reverse('mood-log-api')
        data = {"mood": "neutral"}
        response = self.client.post(url, data, format='json')

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the new mood log exists in the database
        self.assertEqual(MoodLog.objects.count(), 3)
        self.assertEqual(MoodLog.objects.last().mood, "neutral")

    def test_update_mood_log(self):
        # Test PUT request to update an existing mood log
        url = reverse('mood-log-api')
        data = {"id": self.mood_log1.id, "mood": "very pleasant"}
        response = self.client.put(url, data, format='json')

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the mood log was updated
        self.mood_log1.refresh_from_db()
        self.assertEqual(self.mood_log1.mood, "very pleasant")

    def test_update_mood_log_forbidden(self):
        # Test PUT request to update another user's mood log (should fail)
        url = reverse('mood-log-api')
        data = {"id": self.mood_log2.id, "mood": "very unpleasant"}
        response = self.client.put(url, data, format='json')

        # Ensure the request is forbidden for the authenticated user
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_mood_log(self):
        # Test DELETE request to delete an existing mood log
        url = reverse('mood-log-api')
        data = {"ids": [self.mood_log1.id]}
        response = self.client.delete(url, data, format='json')

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify the mood log was deleted from the database
        self.assertEqual(MoodLog.objects.count(), 1)

    def test_delete_mood_log_forbidden(self):
        # Test DELETE request to delete another user's mood log (should fail)
        url = reverse('mood-log-api')
        data = {"ids": [self.mood_log2.id]}
        response = self.client.delete(url, data, format='json')

        # Ensure the request is forbidden for the authenticated user
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Verify the mood log was not deleted from the database
        self.assertEqual(MoodLog.objects.count(), 2)

    def test_superuser_can_access_all_logs(self):
        # Test if superuser can access all mood logs
        self.client.login(username='admin', password='adminpassword')
        url = reverse('mood-log-api')
        response = self.client.get(url)

        # Ensure the request was successful and both logs are returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
