from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record

from .forms import SignUpForm


# Create your views here.

def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in successfully.")
            return redirect('home')
        else:
            messages.success(request, "Username or Password is incorrect. Please input the correct details")
            return redirect('home')
        

    return render(request, 'home.html', {'records':records}) 

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You are registered succesfully! Start now!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form}) 

def logout_user(request):
    logout(request)
    messages.success(request, "You're successfully logout.")
    return redirect('home')