from dataclasses import fields
from pyexpat import model
from pkg_resources import require
from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from django.core.validators import validate_email

from myapp.models import Orders


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    
    class Meta:
        model = User
        fields = '__all__'
        
        extra_kwargs = {
            'password':{'write_only': True}, 'first_name': {'required': True}, 'last_name': {'required': True}, 'email_name': {'required': True}
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password = validated_data['password'], email=validated_data['email'], first_name=validated_data['first_name'],  last_name=validated_data['last_name'])
        return user


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'     


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']