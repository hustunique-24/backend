from django.contrib.auth import get_user_model
from django.shortcuts import render
# Create your views here.
from rest_framework.generics import CreateAPIView

from main.models import User,message
from main.serializers import UserSerializer
from main.serializers import MessageSerializer
from rest_framework import viewsets

# 注册
class CreatUserView(CreateAPIView):
    module = get_user_model()
    serializer_class = UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = message.objects.all()
    serializer_class = MessageSerializer
# Create your views here.
