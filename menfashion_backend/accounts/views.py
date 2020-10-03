from rest_framework import generics
# Create your views here.
from accounts.serializers import UserSerializer,AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from django.contrib.auth.signals import user_logged_in
from rest_framework.response import Response

from accounts.models import User
from django.contrib.auth.models import Group


from rest_framework.mixins import UpdateModelMixin



class CreateUserView(generics.CreateAPIView):
    """create new user in the system"""
    serializer_class = UserSerializer

    # def create(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     print(instance)
    #     # instance.isowner = True
    #     # g = Group.objects.get(name='owner')
    #     # g.user_set.add(instance)
    #     # serializer = AuthTokenSerializer(data=request.data)
    #     # serializer.is_valid(raise_exception=True)
    #     # instance.save()
    #         #
    #     return Response({'isowner':'true'})

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data,})


class CreateOwnerView(generics.UpdateAPIView):
    """create new user in the system"""
    serializer_class = AuthTokenSerializer
    queryset = User.objects.all()
    model = User



    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.isowner = True
        g = Group.objects.get(name='owner')
        g.user_set.add(instance)
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.save()
            #
        return Response({'isowner':'true'})
