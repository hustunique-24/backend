from django.contrib.auth import get_user_model
from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from main.models import UserProfile, message,WenShi
from main.serializers import UserSerializer
from main.serializers import UserProfileSerializer
from main.serializers import MessageSerializer
from main.serializers import WenDu_Serializer
from rest_framework import viewsets, generics, permissions, mixins, serializers


# class WenshiList(viewsets.ModelViewSet):
#     queryset = WenShi.objects.all()
#     serializer_class = WenDu_Serializer

class WenshiList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = WenShi.objects.all().order_by('-Time')
    serializer_class = WenDu_Serializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class Message_Up_List(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = message.objects.all().order_by('-time')
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request)
        return self.create(request, *args, **kwargs)



class Message_Up_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny,)


class CreatUserView(CreateAPIView):
    module = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'userprofile': reverse('userprofile-list', request=request, format=format),
        'register': reverse('register', request=request, format=format),
        'up-message': reverse('message-up-list', request=request, format=format),
        'WenshiList':reverse('WenshiList',request=request, format=format)
    })
