from rest_framework import serializers
from .models import SessionAction, SessionActionDetails, SessionLocationDetails, Resolution


class ResolutionSerializer(serializers.ModelSerializer):
    width = serializers.IntegerField(required=True)
    height = serializers.IntegerField(required=True)

    class Meta:
        model = Resolution
        fields = ('width', 'height')


class SessionActionSerializer(serializers.ModelSerializer):
    resolution = ResolutionSerializer()

    class Meta:
        model = SessionAction
        fields = ('ip', 'resolution')

    def create(self, validated_data):
        resolution = ResolutionSerializer(data=validated_data.get('resolution'))
        resolution.is_valid()
        resolution_instance = resolution.save()
        return SessionAction.objects.create(ip=validated_data['ip'], resolution=resolution_instance)


class SessionLocationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionLocationDetails
        fields = ('longitude', 'latitude', 'city', 'region', 'country', 'country_iso2', 'continent')


class SessionActionDetailsSerializer(serializers.ModelSerializer):
    info = SessionActionSerializer(read_only=True)
    location = SessionLocationDetailsSerializer(read_only=True)

    class Meta:
        model = SessionActionDetails
        fields = ('action', 'info', 'location', 'action_date')
