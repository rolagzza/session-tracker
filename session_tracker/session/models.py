from django.db import models
from django.utils import timezone


class Resolution(models.Model):
    width = models.IntegerField(null=False, blank=False, default=0)
    height = models.IntegerField(null=False, blank=False, default=0)


class SessionAction(models.Model):
    ip = models.GenericIPAddressField()
    resolution = models.OneToOneField(Resolution, on_delete=models.CASCADE)


class SessionLocationDetails(models.Model):
    longitude = models.FloatField(null=False, blank=False, default=0.0)
    latitude = models.FloatField(null=False, blank=False, default=0.0)
    city = models.CharField(null=False, blank=False, max_length=50)
    region = models.CharField(null=False, blank=False, max_length=50)
    country = models.CharField(null=False, blank=False, max_length=50)
    country_iso2 = models.CharField(null=False, blank=False, max_length=50)
    continent = models.CharField(null=False, blank=False, max_length=50)


class SessionActionDetails(models.Model):
    class SessionActionType(models.TextChoices):
        LOGIN = 'LOGIN', 'LOGIN'
        LOGOUT = 'LOGOUT', 'LOGOUT'
        BUY = 'BUY', 'BUY'
        REVIEW = 'REVIEW', 'REVIEW'
        SHOPPING_CART = 'SHOPPING-CART', 'SHOPPING-CART'

    action = models.CharField(choices=SessionActionType.choices, default=SessionActionType.LOGIN,
                              max_length=15)
    info = models.OneToOneField(SessionAction, on_delete=models.CASCADE)
    location = models.OneToOneField(SessionLocationDetails, on_delete=models.CASCADE)
    action_date = models.DateTimeField(default=timezone.now)
