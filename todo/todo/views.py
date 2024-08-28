from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import Todo

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

    return render(request, 'login.html')