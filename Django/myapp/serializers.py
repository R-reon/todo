from django.contrib.auth.models import User

from .models import PileColor, Myapp, Comment
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'password', 'is_active', 'is_superuser')


class PileColorSerializer(serializers.ModelSerializer):
    """ A serializer for the PileColor model """
    class Meta:
        model = PileColor
        fields = ('id', 'name', 'description')


class MyappSerializer(serializers.ModelSerializer):
    """ A serializer for the Myapp Model """
    class Meta:
        model = Myapp
        fields = ('id', 'name', 'pile_color', 'stars', 'description', 'created')


class CommentSerializer(serializers.ModelSerializer):
    """ Serializer for the Comment model """
    class Meta:
        model = Comment
        fields = ('id', 'user', 'myapp', 'comment', 'visible', 'created')