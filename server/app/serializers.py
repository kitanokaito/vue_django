from django.contrib.auth.models import User

from .models import Store, Good, Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('handle_name', 'image', 'comment')

class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username','password', 'is_active', 'is_superuser', 'profile')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'body', 'image', 'user', 'created_at', 'updated_at')

class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('id', 'from_user', 'to_store', 'created_at')