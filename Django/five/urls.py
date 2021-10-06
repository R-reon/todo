from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.todo, name='todo'),
    path('open_todo/', views.OpenTodo, name='open_todo'),
]