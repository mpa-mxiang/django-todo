from django.shortcut import render, redirect

def signup(request):
    return render(request, 'signup.html')