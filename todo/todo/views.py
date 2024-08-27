from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import Todo

def signup(request):
    if request.method=="POST":
        frm = request.POST.get('frm')
        email_id = request.POST.get('emailId')
        pwd = request.POST.get('pwd')
        new_user = User.object.create_user(frm, email_id, pwd)
        new_user.save()

    return render(request, 'signup.html')