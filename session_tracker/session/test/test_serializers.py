from django.test import TestCase
from django.forms.models import model_to_dict
from nose.tools import eq_, ok_
from .factories import ResolutionFactory, SessionActionFactory, SessionLocationDetailsFactory
from ..serializers import ResolutionSerializer, SessionActionSerializer, SessionLocationDetailsSerializer


class TestResolutionSerializer(TestCase):
    def setUp(self):
        self.resolution_data = model_to_dict(ResolutionFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = ResolutionSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = ResolutionSerializer(data=self.resolution_data)
        ok_(serializer.is_valid())

    def test_serializer_with_invalid_data(self):
        self.resolution_data['width'] = 'invalid_integer'
        serializer = ResolutionSerializer(data=self.resolution_data)
        eq_(serializer.is_valid(), False)
        eq_(str(serializer.errors['width'][0]), 'A valid integer is required.')


class TestSessionActionSerializer(TestCase):

    def setUp(self):
        self.resolution_data = model_to_dict(ResolutionFactory.build())
        self.session_action_data = model_to_dict(SessionActionFactory.build())
        self.session_action_data['resolution'] = self.resolution_data

    def test_serializer_with_empty_data(self):
        serializer = SessionActionSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = SessionActionSerializer(data=self.session_action_data)
        ok_(serializer.is_valid())

    def test_serializer_with_invalid_ip_data(self):
        self.session_action_data['ip'] = 'invalid_ip'
        serializer = SessionActionSerializer(data=self.session_action_data)
        eq_(serializer.is_valid(), False)
        eq_(str(serializer.errors['ip'][0]), 'Enter a valid IPv4 or IPv6 address.')


class TestSessionLocationDetailsSerializer(TestCase):

    def setUp(self):
        self.session_location_data = model_to_dict(SessionLocationDetailsFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = SessionLocationDetailsSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = SessionLocationDetailsSerializer(data=self.session_location_data)
        ok_(serializer.is_valid())
