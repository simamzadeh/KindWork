import json
import os
from django.test import TestCase, RequestFactory
from unittest.mock import patch, mock_open
from ..views.utils import get_csrf_token, get_manifest, global_settings, index

class UtilsTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()  # Create a RequestFactory instance
        self.request = self.factory.get('/')  # Create a mock GET request

    def test_get_csrf_token(self):
        response = get_csrf_token(self.request)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"success": "CSRF cookie set"})

    @patch("builtins.open", new_callable=mock_open, read_data='{"files": {"main.js": "/static/js/main.js"}}')
    def test_get_manifest_valid_file(self, mock_file):
        result = get_manifest("main.js")
        self.assertEqual(result, "/static/js/main.js")
        mock_file.assert_called_once_with("kind_app/asset-manifest.json")

    def test_get_manifest_invalid_file(self):
        # Create a temporary file that does not exist
        result = get_manifest("unknown.js")
        self.assertEqual(result, "unknown.js")

    def test_global_settings(self):
        response = global_settings(self.request)
        self.assertEqual(response, {"DOMAIN": "http://localhost:8000"})  # Adjust the expected domain accordingly

    def test_index_view(self):
        response = self.client.get('/')  # Use the test client to make a GET request to the index view
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
