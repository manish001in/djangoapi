from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class ListTests(APITestCase):
    def test_list(self):
        User.objects.create_superuser('manish.rastogi', 'web@localhost.com', 'Ishi@321')
        self.client.login(username='manish.rastogi', password='Ishi@321')
        responseD = self.client.get('/detail/', format='json')
        self.assertEqual(responseD.status_code, status.HTTP_200_OK)
        responseU = self.client.get('/users/', format='json')
        self.assertEqual(responseU.data['count'], 1)
        self.assertEqual(responseU.status_code, status.HTTP_200_OK)


class CRUDTests(APITestCase):
    def test_detail_CRUD(self):
        User.objects.create_superuser('manish.rastogi', 'web@localhost.com', 'Ishi@321')
        self.client.login(username='manish.rastogi', password='Ishi@321')
        responseC = self.client.post('/detail/', {"name": "qwerty", "designation": "asdf", "alive": True}, format='json')
        self.assertEqual(responseC.status_code, status.HTTP_201_CREATED)
        responseR = self.client.get('/detail/1/', format='json')
        self.assertEqual(responseR.status_code, status.HTTP_200_OK)
        self.assertEqual(responseR.data['name'], "qwerty")
        responseU = self.client.put('/detail/1/', {"name": "wety", "designation": "asd", "alive": False}, format='json')
        self.assertEqual(responseU.status_code, status.HTTP_200_OK)
        self.assertEqual(responseU.data['name'], "wety")
        self.assertEqual(responseU.data['designation'], "asd")
        self.assertEqual(responseU.data['alive'], False)
        self.client.post('/detail/', {"name": "rty", "designation": "af", "alive": True}, format='json')
        responseD = self.client.delete('/detail/1/')
        responseR = self.client.get('/detail/1/', format='json')
        self.assertEqual(responseD.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(responseR.status_code, status.HTTP_404_NOT_FOUND)


class UserTests(APITestCase):
    def test_user_check(self):
        User.objects.create_superuser('manish.rastogi', 'web@localhost.com', 'Ishi@321')
        self.client.login(username='manish.rastogi', password='Ishi@321')
        responseC = self.client.post('/detail/', {"name": "qwerty", "designation": "asdf", "alive": True}, format='json')
        self.assertEqual(responseC.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/users/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], "manish.rastogi")



