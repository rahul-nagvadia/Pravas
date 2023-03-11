from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import City, user
from tours.models import Tour


def home_view(request):
    cities = City.objects.all()
    tours = Tour.objects.all()
    context = {'cities': cities, 'tours': tours}
    return render(request, "home.html", context=context)


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
            messages.success(request, "Registration is successfull.")
            return redirect("pravas:home")
        messages.error(request, "Unsuccessfull registration.")

    form = UserRegistration()
    return render(request=request, template_name="register.html", context={"register_form": form})


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
                return redirect("pravas:home")
            else:
                messages.error(request, "Invalid username and password.")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logout.")
    return redirect("pravas:home")
