from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer
from django.contrib.auth.models import User


class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = User.USERNAME_FIELD


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id, name, email', 'password')
