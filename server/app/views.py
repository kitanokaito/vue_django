from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import Store
from .serializers import UserSerializer, StoreSerializer


class UserList(generics.ListAPIView):
    # view to list all user
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
    # view to create new user only accept only POST
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    # view to retrieve and update Accepts GET and PUT requests and the record id must be provided in the request
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class StoreListCreate(generics.ListCreateAPIView):
    
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (permissions.IsAdminUser,)


