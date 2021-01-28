from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from users.models import CustomUser

from .models import GENDER_CHOICES


class CustomUserRegistrationSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=100)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    phone_number = serializers.CharField(max_length=40)
    net_worth = serializers.CharField(max_length=255)
    country = CountryField()

    # rollback save operation incase of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.name = self.data.get("name")
        user.gender = self.data.get('gender')
        user.phone_number = self.data.get("phone_number")
        user.country = self.data.get("country")
        user.net_worth = self.data.get("net_worth")
        user.save()
        return user


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['pk', 'email', 'name', 'phone_number',
                  'gender', 'country', 'net_worth']
        read_only_fields=['pk','email','name','net_worth']          
