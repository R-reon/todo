from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import PileColor, HedgeHog, Comment, TodoModel
from .serializers import UserSerializer, PileColorSerializer, HedgeHogSerializer, CommentSerializer

from django.views import generic
# from .models import TodoModel
from django.urls import reverse_lazy

class UserList(generics.ListAPIView):
    """ View to list all users"""
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    #permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
    """ View to create a new user. Only accepts POST requests """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (permissions.IsAdminUser, )


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve a user or update user information.
    Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (permissions.IsAuthenticated, )


class PileColorListCreate(generics.ListCreateAPIView):
    """ List and create PileColors """
    queryset = PileColor.objects.all()
    serializer_class = PileColorSerializer
    #permission_classes = (permissions.IsAuthenticated, )


class PileColorRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve and update PileColor information """
    queryset = PileColor.objects.all()
    serializer_class = PileColorSerializer
    #permission_classes = (permissions.IsAuthenticated, )


class HedgeHogListCreate(generics.ListCreateAPIView):
    """List and create HedgeHogs """
    queryset = HedgeHog.objects.all().order_by('name')
    serializer_class = HedgeHogSerializer
    #permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        queryset = HedgeHog.objects.all()
        color = self.request.query_params.get('color', None)
        if color is not None:
            queryset = queryset.filter(pile_color=color)
        return queryset

class HedgeHogRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Retrieve and update a HedgeHog"""
    queryset = HedgeHog.objects.all()
    serializer_class = HedgeHogSerializer
    #permission_classes = (permissions.IsAuthenticated, )


class CommentListCreate(generics.ListCreateAPIView):
    """ List or create a HedgeHog """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = (permissions.IsAuthenticated, )


class CommentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ List or create a HedgeHog """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = (permissions.IsAuthenticated, )


class TodoList(generic.ListView):
    template_name = 'hedgehog/list.html'
    model = TodoModel


class TodoDetail(generic.DetailView):
    template_name = 'hedgehog/detail.html'
    model = TodoModel

class TodoUpdate(generic.UpdateView):
    template_name = 'hedgehog/update.html'
    model = TodoModel
    fields = ('title', 'content', 'deadline')
    success_url = reverse_lazy('list')

class TodoDelete(generic.DeleteView):
    template_name = 'hedgehog/delete.html'
    model = TodoModel

    success_url = reverse_lazy('list')

class TodoCreate(generic.CreateView):
    template_name = 'hedgehog/create.html'
    model = TodoModel
    fields = ('title', 'content', 'deadline')

    success_url = reverse_lazy('list')