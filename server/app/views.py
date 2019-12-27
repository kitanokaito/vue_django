from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Store, Good, Profile
from .serializers import UserSerializer, StoreSerializer, GoodSerializer, ProfileSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request):
        del request.data['passwordConfirm']
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(status=status.HTTP_200_OK)

class StoreListCreate(generics.ListCreateAPIView):
    
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (permissions.AllowAny,)

    def list(self, request):
        data = []
        ids = self.get_queryset().order_by('-pk').values_list('pk', flat=True)
        for store_id in ids:
            from_user_id = Store.objects.values_list('user', flat=True).get(pk=store_id)
            profile = Profile.objects.filter(user=from_user_id).first()
            profile = ProfileSerializer(profile).data
            store = self.get_queryset().filter(pk=store_id).first()
            post = StoreSerializer(store).data
            post.update(profile)
            data.append(post)

        return Response(data=data, status=status.HTTP_200_OK)

class StoreListOfUser(generics.ListCreateAPIView):
    
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        username = request.GET.get('username')
        user = User.objects.filter(username=username).first()
        stores = self.get_queryset().filter(user=user)
        data = StoreSerializer(stores, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

class UserList(generics.ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class GoodCreate(generics.ListCreateAPIView):
     
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        
        storeId = request.data['to_store']
        goodObject = Good(from_user_id=request.user.id, to_store_id=storeId)
        goodObject.save()
        return Response(status=status.HTTP_200_OK)

    def list(self, request):
        
        to_store = request.GET.get('to_store')
        data = len(self.get_queryset().filter(to_store=to_store))
        return Response(data=data, status=status.HTTP_200_OK)


class GoodDestroy(generics.RetrieveDestroyAPIView):
     
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def destroy(self, request, store_id):
        self.get_queryset().filter(from_user=request.user.id).filter(to_store=store_id).delete()
        return Response(status=status.HTTP_200_OK)

    def retrieve(self, request, store_id):
        queryset = self.get_queryset().filter(from_user=request.user.id).filter(to_store=store_id)
        data = len(queryset)
        return Response(data=data, status=status.HTTP_200_OK)

class MypageRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def retrieve(self, request):
        data = self.get_queryset().filter(user=request.user)
        data = ProfileSerializer(data, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

