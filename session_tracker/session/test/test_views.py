import json
from mock import patch
from nose.tools import eq_

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .mocks import ip_lookup_data

class TestTrackTestCase(APITestCase):
    """
    Tests /track endpoint
    """

    def setUp(self):
        self.url = reverse('track', kwargs={'action': 'login'})

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_wrong_action_fails(self):
        url = self.url = reverse('track', kwargs={'action': 'invalid-action'})
        response = self.client.post(url, {})
        content = json.loads(response.content)
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)
        eq_(content['errors'], ['This action is not supported'])

    def test_post_request_with_no_ip_data_fails(self):
        payload = {
            'ip': '',
            'resolution': {
                'width': '10',
                'height': '29',
            }
        }
        response = self.client.post(self.url, data=payload, format='json')
        content = json.loads(response.content)
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)
        eq_(content['errors'][0]['ip'], ['This field may not be blank.'])

    def test_post_request_with_wrong_ip_data_fails(self):
        payload = {
            'ip': '222222.33333',
            'resolution': {
                'width': '10',
                'height': '29',
            }
        }
        response = self.client.post(self.url, data=payload, format='json')
        content = json.loads(response.content)
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)
        eq_(content['errors'][0]['ip'], ['Enter a valid IPv4 or IPv6 address.'])

    def test_post_request_with_no_width_data_fails(self):
        payload = {
            'ip': '1.1.1.1',
            'resolution': {
                'width': '',
                'height': '29',
            }
        }
        response = self.client.post(self.url, data=payload, format='json')
        content = json.loads(response.content)
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)
        eq_(content['errors'][0]['resolution']['width'], ['A valid integer is required.'])

    @patch('session_tracker.session.ip_lookup_client.get_ip_details')
    def test_post_request_with_valid_data_succeed(self, get_ip_details):
        get_ip_details.side_effect = [ip_lookup_data]

        payload = {
            'ip': '1.1.1.1',
            'resolution': {
                'width': '10',
                'height': '29',
            }
        }

        expected_action = 'login'
        expected_info = {
            'ip': '1.1.1.1',
            'resolution': {
                'width': 10, 'height': 29
            }
        }
        expected_location = {
            'longitude': 0.0,
            'latitude': 0.0,
            'city': 'Timișoara',
            'region': 'Timis',
            'country': 'Romania',
            'country_iso2': 'RO',
            'continent': 'EU'
        }

        response = self.client.post(self.url, data=payload, format='json')
        content = json.loads(response.content)
        eq_(response.status_code, status.HTTP_200_OK)
        eq_(content['action'], expected_action)
        eq_(content['info'], expected_info)
        eq_(content['location'], expected_location)
        eq_(get_ip_details.call_count, 1)
