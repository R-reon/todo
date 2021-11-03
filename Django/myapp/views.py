from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import PileColor, Myapp, Comment
from .serializers import UserSerializer, PileColorSerializer, MyappSerializer, CommentSerializer


class UserList(generics.ListAPIView):
    """ View to list all users"""
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
    """ View to create a new user. Only accepts POST requests """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve a user or update user information.
    Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

class PileColorListCreate(generics.ListCreateAPIView):
    """ List and create PileColors """
    queryset = PileColor.objects.all()
    serializer_class = PileColorSerializer
    permission_classes = (permissions.IsAuthenticated, )


class PileColorRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve and update PileColor information """
    queryset = PileColor.objects.all()
    serializer_class = PileColorSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MyappListCreate(generics.ListCreateAPIView):
    """List and create Myapp """
    queryset = Myapp.objects.all().order_by('name')
    serializer_class = MyappSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MyappRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Retrieve and update a Myapp"""
    queryset = Myapp.objects.all()
    serializer_class = MyappSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CommentListCreate(generics.ListCreateAPIView):
    """ List or create a Myapp """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CommentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ List or create a Myapp """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, )