from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import Todo
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

def signup(request):

    error_message = None    
    if request.method == "POST":
        frm = request.POST.get('frm')
        email_id = request.POST.get('emailId')
        pwd = request.POST.get('pwd')
        
        try:
            new_user = User.objects.create_user(frm, email_id, pwd)
            new_user.save()
            return redirect('/login')
        except IntegrityError:
            error_message = "Username already exists. Please choose a different username."
    
    return render(request, 'signup.html', {'error_message': error_message})


def login(request):

    error_message = None    
    if request.method == "POST":
        frm = request.POST.get('frm')
        pwd = request.POST.get('pwd')
        login_user = authenticate(request, username=frm, password=pwd)
        if login_user is not None:
            return redirect('/todo')
        else:
            error_message = "Wrong Username and/or Password, please try it again."
    
    return render(request, 'login.html', {'error_message': error_message})

def todo(request):
    if request.method=="POST":
        title = request.POST.get('title')
        task = models.Todo(title=title, user=request.user)
        task.save()
    return render(request, "todo.html")