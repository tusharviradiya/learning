from rest_framework import serializers
from app.models import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ("id", "username", "email", "phone", "password")

    def __str__(self):
        return self.username
