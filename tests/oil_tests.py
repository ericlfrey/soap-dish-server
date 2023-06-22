from rest_framework import status
from rest_framework.test import APITestCase


class OilTests(APITestCase):
    """Test the Oil API"""
    fixtures = ['oils']

    def test_get_all_oils(self):
        """GET all oils"""
        response = self.client.get('/oils')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_oil(self):
        """GET single oil"""
        response = self.client.get('/oils/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
