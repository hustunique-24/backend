from django.shortcuts import render
# Create your views here.
from main.models import User, message
from main.serializers import UserSerializer
from main.serializers import MessageSerializer
from rest_framework import viewsets


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = message.objects.all()
    serializer_class = MessageSerializer
# Create your views here.
