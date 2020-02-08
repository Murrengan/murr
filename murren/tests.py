import os
import shutil

from django.conf import settings
from django.urls import reverse

# rest
from rest_framework import status
from rest_framework.test import APITestCase

# local
from murren.models import Murren


class MurrenAccountTests(APITestCase):

    def setUp(self) -> None:
        settings.EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
        settings.EMAIL_FILE_PATH = 'tests/send_email_reset_password'
        data = {'username': 'Test',
                'email': 'murren_test@gmail.com',
                'password': "werty52@@_dfe"}

        Murren.objects.create_user(**data)

    def test_create_account(self):
        url = reverse('murren_register')
        data = {'username': 'Test1',
                'email': 'murren_test1@gmail.com',
                'password': "werty52@@_2"}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Murren.objects.filter()[1].username, 'Test1')

    def test_reset_password_and_confirm(self):
        url = reverse('password_reset')
        data = {'email': 'murren_test@gmail.com'}
        email_path = getattr(settings, 'EMAIL_FILE_PATH')

        if os.path.exists(email_path):
            shutil.rmtree(email_path)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for key, val in response.data.items():
            self.assertTrue(key == 'detail', msg=f'{key}: {val[0]}')

        file = os.path.join(email_path, os.listdir(email_path)[0])

        with open(file, 'r') as f:
            text_mail = f.read()
            start_ind = text_mail.find('http://testserver/confirm-password')
            url = text_mail[start_ind:len(text_mail)].split()[0]
            data = {'new_password1': '1234rte7@_',
                    'new_password2': '1234rte7@_'}

            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            for key, val in response.data.items():
                self.assertTrue(key == 'detail', msg=f'{key}: {val[0]}')



