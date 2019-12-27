from django.contrib.auth.models import User

from .models import Store, Good, Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('handle_name', 'icon', 'comment')


class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'address', 'body', 'image', 'user', 'created_at', 'updated_at')


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('id', 'from_user', 'to_store', 'created_at')