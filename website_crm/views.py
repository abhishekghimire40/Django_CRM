from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Record
# Create your views here.


def home(request):
    records = Record.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in succesfully!")
        else:
            messages.error(request, "There was an error logging in!")
        return redirect("home")
    else:
        return render(request, "home.html", {"records":records,})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect("home")


def register_user(request):
    # user submits the sign up form
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and log them in
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(
                request,
                "Your account has been created successfully! You are logged in now!",
            )
            return redirect("home")
    else:
    # if user only visited this page
        form = SignUpForm()
    return render(request, "register.html", {"form": form})
