from django.contrib.auth import get_user_model
from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from main.models import UserProfile,message
from main.serializers import UserSerializer
from main.serializers import MessageSerializer
from main.serializers import UserProfileSerializer
from rest_framework import viewsets, generics, permissions


class UserProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = message.objects.all()
    serializer_class = MessageSerializer
# Create your views here.

class CreatUserView(CreateAPIView):
    module = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'userprofile': reverse('userprofile-list', request=request, format=format),
        'register': reverse('register', request=request, format=format),
})