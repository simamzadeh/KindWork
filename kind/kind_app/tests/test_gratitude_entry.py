from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from kind_app.models.gratitude_entry import GratitudeEntry

class GratitudeEntryViewTestCase(APITestCase):

    def setUp(self):
        # Create a test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        # Create some sample entries for the user
        self.entry1 = GratitudeEntry.objects.create(user_id=self.user, content="Grateful for coffee")
        self.entry2 = GratitudeEntry.objects.create(user_id=self.user, content="Grateful for the sunshine")

    def test_list_gratitude_entries(self):
        # Test GET request to list entries
        url = reverse('gratitude-entry')
        response = self.client.get(url)

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the correct number of entries is returned
        self.assertEqual(len(response.data), 2)

    def test_create_gratitude_entry(self):
        # Test POST request to create a new entry
        url = reverse('gratitude-entry')
        data = {"content": "Grateful for good health"}
        response = self.client.post(url, data, format='json')

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify that the new entry is in the database
        self.assertEqual(GratitudeEntry.objects.count(), 3)
        self.assertEqual(GratitudeEntry.objects.last().content, "Grateful for good health")

    def test_update_gratitude_entry(self):
        # Test PUT request to update an existing entry
        url = reverse('gratitude-entry')
        data = {"id": self.entry1.id, "content": "Grateful for coffee and books"}
        response = self.client.put(url, data, format='json')

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that the entry was updated
        self.entry1.refresh_from_db()
        self.assertEqual(self.entry1.content, "Grateful for coffee and books")

    def test_delete_gratitude_entry(self):
        # Test DELETE request to delete an existing entry
        url = reverse('gratitude-entry')
        data = {"id": self.entry2.id}
        response = self.client.delete(url, data, format='json')

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify that the entry was deleted from the database
        self.assertEqual(GratitudeEntry.objects.count(), 1)
