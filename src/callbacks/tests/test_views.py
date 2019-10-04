import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Callback
from ..serializers import CallbackSerializer

client = Client()


class GetAllCallbacksTest(TestCase):
    """ Test module for GET all callbacks API """

    def setUp(self):
        Callback.objects.create(
            device='Device 01', snr='7.5', data='Test 01', time='1234')
        Callback.objects.create(
            device='Device 02', snr='9.0', data='Test 02', time='1234')
        Callback.objects.create(
            device='Device 03', snr='8.5', data='Test 03', time='1234')

    def test_get_all_callbacks(self):
        # API response
        response = client.get(reverse('get_post_callbacks'))
        # data from db
        callbacks = Callback.objects.all()
        serializer = CallbackSerializer(callbacks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewCallbackTest(TestCase):
    """ Test module for inserting new callback """

    def setUp(self):
        self.valid_callback = {
            'device': 'Device 01',
            'snr': 4.75,
            'data': 'Data 01',
            'time': '12345'
        }
        self.invalid_callback = {
            'device': '',
            'snr': 444.222,
            'data': 'Data 02',
            'time': '4321'
        }

    def test_create_valid_callback(self):
        response = client.post(
            reverse('get_post_callbacks'),
            data=json.dumps(self.valid_callback),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_callback(self):
        response = client.post(
            reverse('get_post_callbacks'),
            data=json.dumps(self.invalid_callback),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
