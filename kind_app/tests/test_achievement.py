from django.test import TestCase, Client, override_settings
from django.contrib.auth.models import User
from django.urls import reverse
from kind_app.models.achievement import Achievement

@override_settings(AXES_ENABLED=False)
class AchievementViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.achievement_url = reverse('achievements-api')  # URL for the list and create endpoint
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')

    def test_achievement_GET_user_not_authenticated(self):
        response = self.client.get(self.achievement_url)
        self.assertEqual(response.status_code, 403)

    def test_achievement_GET_user_authenticated_no_accounts(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.achievement_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)  # Assert that no entries are returned

    def test_achievement_GET_user_authenticated_with_accounts(self):
        self.client.login(username='testuser', password='password')
        Achievement.objects.create(user=self.user, content='Test Act Content')
        response = self.client.get(self.achievement_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # Ensure that we received one entry

    def test_achievement_GET_admin_user(self):
        admin_user = User.objects.create_superuser(username='adminuser', email='admin@example.com', password='adminpass')
        self.client.login(username='adminuser', password='adminpass')
        Achievement.objects.create(user=self.user, content='User Act Content')
        Achievement.objects.create(user=admin_user, content='Admin Act Content')
        response = self.client.get(self.achievement_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # Assert admin can see both entries

    def test_achievementt_POST_authenticated_user(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.achievement_url, {'content': 'New Act Content'})
        self.assertEqual(response.status_code, 201)  # Check for success response
        self.assertEqual(Achievement.objects.count(), 1)  # Assert one achievement created
        self.assertEqual(Achievement.objects.first().content, 'New Act Content')  # Verify content

    def test_achievement_PUT_authenticated_user(self):
        self.client.login(username='testuser', password='password')
        achievement = Achievement.objects.create(user=self.user, content='Old Content')
        response = self.client.put(self.achievement_url, {'id': achievement.pk, 'content': 'Updated Content'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)  # Expecting success for updating
        achievement.refresh_from_db()  # Refresh to get the updated instance
        self.assertEqual(achievement.content, 'Updated Content')  # Assert the content has been updated

    def test_achievement_DELETE_authenticated_user(self):
        self.client.login(username='testuser', password='password')
        achievement = Achievement.objects.create(user=self.user, content='Delete Me Content')
        response = self.client.delete(self.achievement_url, {'ids': [achievement.pk]}, content_type='application/json')
        self.assertEqual(response.status_code, 204)  # Expecting no content response
        self.assertEqual(Achievement.objects.count(), 0)  # Assert the achievement has been deleted
