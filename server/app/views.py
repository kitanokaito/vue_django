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



class StoreListCreate(generics.ListCreateAPIView):
    
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (permissions.IsAdminUser,)

class StoreListOfUser(generics.ListCreateAPIView):
    
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (permissions.IsAdminUser,)

    def list(self, request):
        username = request.GET.get('username')
        user = User.objects.filter(username=username).first()
        stores = self.get_queryset().filter(user=user)
        data = StoreSerializer(stores, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

class GoodCreate(generics.ListCreateAPIView):
     
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = (permissions.IsAdminUser,)

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
    permission_classes = (permissions.IsAdminUser,)

    def destroy(self, request, store_id):
        self.get_queryset().filter(from_user=request.user.id).filter(to_store=store_id).delete()
        return Response(status=status.HTTP_200_OK)

    def retrieve(self, request, store_id):
        queryset = self.get_queryset().filter(from_user=request.user.id).filter(to_store=store_id)
        data = len(queryset)
        return Response(data=data, status=status.HTTP_200_OK)

