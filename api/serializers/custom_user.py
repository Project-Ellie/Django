from django.contrib.auth import get_user_model
from rest_framework import serializers


class CustomUserApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
