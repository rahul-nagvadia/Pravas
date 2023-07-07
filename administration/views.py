from datetime import date, datetime
from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from vacation_package.models import Place, Month


def home_view(request):
    places = Place.objects.all
    months = Month.objects.all
    return render(request, "administration/index.html", {'places': places, 'months': months})


def register_request(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            user = form.save(commit=False)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            login(request, user)
            messages.success(request, "Registration is successful.")
            return redirect("administration:home")
        messages.error(request, "Unsuccessful registration.")

    form = UserRegistration()
    return render(request=request, template_name="administration/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in ans {username}")
                return redirect("administration:home")
            else:
                messages.error(request, "Invalid username and password.")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="administration/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logout.")
    return redirect("administration:home")


@login_required
def profile_request(request):
    user = request.user
    if request.method == 'POST':
        if request.POST.get('first_name'):
            user.first_name = request.POST['first_name']
        if request.POST.get('last_name'):
            user.last_name = request.POST['last_name']
        if request.POST.get('email'):
            user.email = request.POST['email']
        user.save()
        messages.success(request, 'Your profile has been updated.')
        return redirect('administration:profile')
    return render(request=request, template_name="administration/profile.html")


@login_required
def update_user(request):
    user = request.user
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'update_user.html', {'form': form})
