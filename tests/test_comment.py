from rest_framework import status
from rest_framework.test import APITestCase


class CommentTests(APITestCase):
    """Test the Comment API"""
    fixtures = ['comments', 'recipes', 'soapers']

    def test_get_single_comment(self):
        """GET single comment"""
        response = self.client.get('/comments/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
