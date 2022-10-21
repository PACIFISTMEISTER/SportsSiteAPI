from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from AuthApp.serialziers import CreateUser
from AuthApp.token import MyToken


class login(TokenObtainPairView):
    """логин"""
    serializer_class = MyToken


class signin(generics.CreateAPIView):
    """регистарция"""
    serializer_class = CreateUser
