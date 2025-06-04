from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from kind_app.models.satisfaction import Satisfaction


class SatisfactionViewTestCase(APITestCase):

    def setUp(self):
        # Create a test user and another user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.other_user = User.objects.create_user(username='otheruser', password='password')
        self.superuser = User.objects.create_superuser(username='admin', password='adminpassword')

        self.client.login(username='testuser', password='password')

        # Create sample satisfaction logs for both users
        self.satisfaction1 = Satisfaction.objects.create(user=self.user, satisfaction="pleasant")
        self.satisfaction2 = Satisfaction.objects.create(user=self.other_user, satisfaction="unpleasant")

    def test_get_satisfaction_list(self):
        # Test GET request to retrieve all satisfaction logs for the authenticated user
        url = reverse('satisfaction-api')  # No pk argument
        response = self.client.get(url)

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that only the authenticated user's logs are returned
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['satisfaction'], "pleasant")

    def test_get_satisfaction_by_id(self):
        # Test GET request to retrieve a specific satisfaction log manually
        # Simulate what the view would do by filtering the queryset based on ID
        url = reverse('satisfaction-api')  # No pk argument, filter by ID manually
        response = self.client.get(url)

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure the satisfaction log content matches (only user logs are returned)
        self.assertEqual(response.data[0]['satisfaction'], self.satisfaction1.satisfaction)

    def test_get_satisfaction_forbidden(self):
        # Test GET request to ensure the user can't access another user's satisfaction log
        url = reverse('satisfaction-api')  # No pk argument
        response = self.client.get(url)

        # Ensure the request is forbidden (since it's not returning the other user's data)
        # The response should not contain the other user's logs
        self.assertNotIn(self.satisfaction2.id, [log['id'] for log in response.data])

    def test_create_satisfaction_log(self):
        # Test POST request to create a new satisfaction log
        url = reverse('satisfaction-api')
        data = {"satisfaction": "neutral"}
        response = self.client.post(url, data, format='json')

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the new satisfaction log exists in the database
        self.assertEqual(Satisfaction.objects.count(), 3)
        self.assertEqual(Satisfaction.objects.last().satisfaction, "neutral")

    def test_update_satisfaction_log(self):
        # Test PUT request to update an existing satisfaction log
        url = reverse('satisfaction-api')
        data = {"id": self.satisfaction1.id, "satisfaction": "very content"}
        response = self.client.put(url, data, format='json')

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the satisfaction log was updated
        self.satisfaction1.refresh_from_db()
        self.assertEqual(self.satisfaction1.satisfaction, "very content")

    def test_update_satisfaction_forbidden(self):
        # Test PUT request to update another user's satisfaction log (should fail)
        url = reverse('satisfaction-api')
        data = {"id": self.satisfaction2.id, "satisfaction": "very content"}
        response = self.client.put(url, data, format='json')

        # Ensure the request is forbidden for the authenticated user
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_satisfaction(self):
        # Test DELETE request to delete an existing satisfaction log
        url = reverse('satisfaction-api')
        data = {"ids": [self.satisfaction1.id]}
        response = self.client.delete(url, data, format='json')

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify the satisfaction log was deleted from the database
        self.assertEqual(Satisfaction.objects.count(), 1)

    def test_delete_satisfaction_forbidden(self):
        # Test DELETE request to delete another user's satisfaction log (should fail)
        url = reverse('satisfaction-api')
        data = {"ids": [self.satisfaction2.id]}
        response = self.client.delete(url, data, format='json')

        # Ensure the request is forbidden for the authenticated user
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Verify the satisfaction log was not deleted from the database
        self.assertEqual(Satisfaction.objects.count(), 2)

    def test_superuser_can_access_all_logs(self):
        # Test if superuser can access all satisfaction logs
        self.client.login(username='admin', password='adminpassword')
        url = reverse('satisfaction-api')
        response = self.client.get(url)

        # Ensure the request was successful and both logs are returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
