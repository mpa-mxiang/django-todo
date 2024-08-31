from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import Todo
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


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


def user_logn(request):

    error_message = None
    if request.method == "POST":
        frm = request.POST.get('frm')
        pwd = request.POST.get('pwd')
        login_user = authenticate(request, username=frm, password=pwd)
        if login_user is not None:
            login(request, login_user)
            return redirect('/todo')
        else:
            error_message = "Wrong Username and/or Password, please try it again."

    return render(request, 'login.html', {'error_message': error_message})


@login_required(login_url='/login')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        obj = models.Todo(title=title, user=request.user)
        obj.save()
        user = request.user
        res = models.Todo.objects.filter(user=user).order_by('-date')
        return redirect('/todo', {'res': res})

    res = models.Todo.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res, })


def edit_todo(request, srno):
    # Fetch the todo item to be edited
    obj = models.Todo.objects.get(srno=srno)

    if request.method == 'POST':
        # Update the title of the todo item
        title = request.POST.get('title')
        obj.title = title
        obj.save()

        # Fetch updated list of tasks for the logged-in user
        user = request.user
        res = models.Todo.objects.filter(user=user).order_by('-date')

        # Redirect back to the todo page
        return redirect('/todo')

    # If it's a GET request, render the todo page
    res = models.Todo.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html',{'res':res,})
