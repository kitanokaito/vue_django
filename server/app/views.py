from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Store, Good
from .serializers import UserSerializer, StoreSerializer, GoodSerializer

class MultipleFieldLookupMixin(object):
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            filter[field] = self.kwargs[field]

        return get_object_or_404(queryset, **filter)  # Lookup the object


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


class GoodCreate(generics.CreateAPIView):
     
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = (permissions.IsAdminUser,)

    def create(self, request, *args, **kwargs):
        
        storeId = request.data['to_store']
        goodObject = Good(from_user_id=request.user.id, to_store_id=storeId)
        goodObject.save()

        return Response(status=status.HTTP_200_OK)


class GoodDestroy(generics.DestroyAPIView):
     
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = (permissions.IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        
        queryset = self.get_queryset()
        to_store = request.GET.get('to_store')
        Good.objects.filter(from_user=request.user.id).filter(to_store=to_store).delete()

        return Response(status=status.HTTP_200_OK)

class GoodStatus(generics.RetrieveAPIView):
     
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = (permissions.IsAdminUser,)

    def retrieve(self, request):
        storeId = request.GET.get('to_store')
        queryset = Good.objects.filter(from_user=request.user.id).filter(to_store=storeId)
        data = len(queryset)
        return Response(data=data, status=status.HTTP_200_OK)

class GoodNum(generics.ListAPIView):
     
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        to_store = request.GET.get('to_store')
        data = len(Good.objects.filter(to_store=to_store))
        return Response(data=data, status=status.HTTP_200_OK)
