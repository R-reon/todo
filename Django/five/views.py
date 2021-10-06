from django.shortcuts import render

def index(request):
    return render(request, 'five/index.html', {})

def todo(request):
    return render(request, 'five/todo.html', {})

def OpenTodo(request):
    return render(request, 'five/open_todo.html', {})