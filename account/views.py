from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import UserCreationForm, LoginForm
from .models import User, Customer


def register_request(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('/')
        else:
            messages.error(
                request, "Unsuccessful registration. Invalid information.")
    return render(request, 'accounts/register.html', context={'form': form})


def login_request(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f"You are now logged in as {user.get_full_name()}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "accounts/login.html", {"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")
