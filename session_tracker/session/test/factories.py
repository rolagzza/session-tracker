import factory
import datetime

class ResolutionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'session.Resolution'

    width = 12
    height = 13


class SessionActionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'session.SessionAction'

    ip = '1.1.1.1'
    resolution = factory.SubFactory(ResolutionFactory)


class SessionLocationDetailsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'session.SessionLocationDetails'

    longitude = 10
    latitude = 12
    city = 'Timisoara'
    region = 'Timis'
    country = 'Romania'
    country_iso2 = 'RO'
    continent = 'Europe'


class SessionActionDetailsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'session.SessionActionDetails'

    action = 'login'
    info = factory.SubFactory(SessionActionFactory)
    location = factory.SubFactory(SessionLocationDetailsFactory)
    action_date = datetime.datetime.now()
