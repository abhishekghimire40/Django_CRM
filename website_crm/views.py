from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm, AddRecordForm
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
        return render(
            request,
            "home.html",
            {
                "records": records,
            },
        )


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
            login(request, user)
            messages.success(
                request,
                "Your account has been created successfully! You are logged in now!",
            )
            return redirect("home")
    else:
        # if user only visited this page
        form = SignUpForm()
    return render(request, "register.html", {"form": form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(
            request,
            "record.html",
            {
                "customer_record": customer_record,
            },
        )
    else:
        messages.error(request, "Please login to view records!")
        return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        customer_record.delete()
        messages.success(request, "Record has been deleted successfully")
        return redirect("home")
    else:
        messages.error(request, "You have to login first")
        return redirect("home")


def add_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record has been added successfully!")
                return redirect("home")
        else:
            form = AddRecordForm()
        return render(request, "add_record.html", {"form": form})
    else:
        messages.error(request, "You have to login first")
        return redirect("home")

def update_record(request,pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        if request.method == "POST":
            form = AddRecordForm(request.POST,instance=record)
            if form.is_valid():
                form.save()
                messages.success(request,"Record was updated successfully!")
                return redirect('record',pk=pk)
        else:
            form = AddRecordForm(instance=record)
            return render(request,'update_record.html',{"form":form,"record":record})
    
    return redirect('customer_record',pk=pk)