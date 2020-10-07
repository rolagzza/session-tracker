from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from django.utils import timezone

from .models import SessionActionDetails, SessionAction, SessionLocationDetails
from .serializers import SessionActionDetailsSerializer, SessionActionSerializer
from session_tracker.session import ip_lookup_client


class SessionAPIDetailView(generics.ListCreateAPIView):
    queryset = SessionAction.objects.all()
    serializer_class = SessionActionSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # get action type and validate it
        action = self.kwargs.get('action')
        choices = [choice[0] for choice in SessionActionDetails.SessionActionType.choices]
        if action.upper() not in choices:
            errors = {
                'errors': [
                    'This action is not supported'
                ]
            }
            return Response(status=400, data=errors)

        # get session action
        session_action = SessionActionSerializer(data=request.data)
        if not session_action.is_valid():
            errors = {
                'errors': [
                    session_action.errors
                ]
            }
            return Response(status=400, data=errors)
        session_action_instance = session_action.save()

        # get IP details from API
        ip = session_action.data['ip']
        ip_info = ip_lookup_client.get_ip_details(ip)

        # create session location details
        session_location_details_instance = SessionLocationDetails.objects.create(
            longitude=ip_info['ip']['longitude'],
            latitude=ip_info['ip']['latitude'],
            city=ip_info['ip']['city'],
            region=ip_info['ip']['region'],
            country=ip_info['ip']['country_names']['en'],
            country_iso2=ip_info['ip']['country'],
            continent=ip_info['ip']['continent']
        )

        # create session action details
        session_action_details = SessionActionDetails.objects.create(
            action=action,
            info=session_action_instance,
            location=session_location_details_instance,
            action_date=timezone.now(),
        )

        # return newly created data
        serializer = SessionActionDetailsSerializer(session_action_details)
        return Response(serializer.data)
