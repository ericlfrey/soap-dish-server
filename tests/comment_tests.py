import json
from rest_framework import status
from rest_framework.test import APITestCase


class CommentTests(APITestCase):
    """Test the Comment API"""
    fixtures = ['comments', 'recipes', 'soapers']

    def test_get_single_comment(self):
        """GET single comment"""
        response = self.client.get('/comments/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment(self):
        """POST a comment"""
        url = "/comments"
        data = {
            "text": "This is a test comment",
            "soaper": 1,
            "recipe": 1,
            "date_added": "2020-04-01T00:00:00Z"
        }
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            json_response,
            {
                "id": json_response["id"],
                "soaper": 1,
                "recipe": 1,
                "text": "This is a test comment",
                "date_added": "2020-04-01T00:00:00Z",
            }
        )
