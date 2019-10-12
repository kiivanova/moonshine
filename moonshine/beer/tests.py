from django.test import TestCase


class ApiTest(TestCase):
    def test_create_beer(self):
        response = self.client.post('/api/beer/', {'name': 'test_beer',
                                                   'description': 'test_description',
                                                   'beer_type': 'ST'})
        self.assertEqual(response.status_code, 201)
