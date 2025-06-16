from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from kind_app.models.kudos import Kudos


class KudosDetailViewTestCase(APITestCase):

    def setUp(self):
        # Create a test user and another user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.other_user = User.objects.create_user(username='otheruser', password='password')
        self.client.login(username='testuser', password='password')

        # Create sample kudos entries for both users
        self.entry1 = Kudos.objects.create(user=self.user, content="Kudos to John")
        self.entry2 = Kudos.objects.create(user=self.other_user, content="I give kudos to Jane")

    def test_get_kudos_entry_list(self):
        # Test GET request to retrieve all entries for the authenticated user
        url = reverse('kudos-api')  # No pk argument
        response = self.client.get(url)

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that only the authenticated user's entries are returned
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['content'], "Kudos to John")

    def test_get_kudos_entry_by_id(self):
        # Test GET request to retrieve a specific entry by filtering manually
        # The view logic requires a list of entries (this test simulates what the view does)
        entry = Kudos.objects.get(pk=self.entry1.id)
        url = reverse('kudos-api')  # No pk argument
        response = self.client.get(url)

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure the entry content matches
        self.assertEqual(response.data[0]['content'], entry.content)

    def test_get_kudos_entry_forbidden(self):
        # Test GET request to ensure the user can't access another user's entry
        url = reverse('kudos-api')  # No pk argument
        response = self.client.get(url)

        # Ensure the authenticated user can't view the other user's entries
        self.assertNotIn(self.entry2.id, [entry['id'] for entry in response.data])

    def test_create_kudos_entry(self):
        # Test POST request to create a new entry
        url = reverse('kudos-api')
        data = {"content": "Kudos to my manager"}
        response = self.client.post(url, data, format='json')

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the new entry exists in the database
        self.assertEqual(Kudos.objects.count(), 3)
        self.assertEqual(Kudos.objects.last().content, "Kudos to my manager")

    def test_update_kudos_entry(self):
        # Test PUT request to update an entry owned by the user
        url = reverse('kudos-api')
        data = {"id": self.entry1.id, "content": "I give kudos to Tyler"}
        response = self.client.put(url, data, format='json')

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the entry was updated
        self.entry1.refresh_from_db()
        self.assertEqual(self.entry1.content, "I give kudos to Tyler")

    def test_update_kudos_entry_forbidden(self):
        # Test PUT request to update another user's entry (should fail)
        url = reverse('kudos-api')
        data = {"id": self.entry2.id, "content": "Sam deserves kudos"}
        response = self.client.put(url, data, format='json')

        # Ensure the request is forbidden for the authenticated user
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_kudos_entry(self):
        # Test DELETE request to delete an entry owned by the user
        url = reverse('kudos-api')
        data = {"ids": [self.entry1.id]}
        response = self.client.delete(url, data, format='json')

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify the entry was deleted from the database
        self.assertEqual(Kudos.objects.count(), 1)

    def test_delete_kudos_entry_forbidden(self):
        # Test DELETE request to delete another user's entry (should fail)
        url = reverse('kudos-api')
        data = {"ids": [self.entry2.id]}
        response = self.client.delete(url, data, format='json')

        # Ensure the request is forbidden for the authenticated user
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Verify the entry was not deleted from the database
        self.assertEqual(Kudos.objects.count(), 2)
