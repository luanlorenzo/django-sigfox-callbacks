from django.test import TestCase
from ..models import Callback


class CallbackTest(TestCase):
    """ Test module for Callback model """

    def setUp(self):
        Callback.objects.create(
            device='Device 01', snr='7.5', data='Test 01', time='1234')

    def test_callback_create(self):
        callback_01 = Callback.objects.get(device='Device 01')

        self.assertEqual(callback_01.data, 'Test 01')
