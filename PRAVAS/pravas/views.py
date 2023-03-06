from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import user, Ticket, Tour, TicketBooking, TourBooking
# for mail sending
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def home_view(request):
    return render(request, "home.html")


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


def search_ticket(request):
    if not request.user.is_authenticated:
        return redirect("pravas:login")
    context = {}
    if request.method == "POST":
        source = request.POST["source"]
        destination = request.POST["destination"]
        tickets = Ticket.objects.filter(source=source, destination=destination)
        date_booked = request.POST["date_booked"]
        quantity = request.POST["quantity"]
        context = {'tickets': tickets,
                   'date_booked': date_booked, 'quantity': quantity}
        return render(request=request, template_name="search.html", context=context)
    return redirect("pravas:home")


def book_ticket(request):
    context = {}
    if request.method == "POST":
        ticket_id = request.POST["ticket_id"]
        ticket = Ticket.objects.get(id=ticket_id)
        date_booked = request.POST["date_booked"]
        quantity = request.POST["quantity"]
        user = request.user
        booking_obj = TicketBooking(
            user=user, ticket=ticket, quantity=quantity, date_booked=date_booked)
        booking_obj.save()
        messages.success(request, "Ticket book successfully.")
        subject = 'Your Ticket!'
        message = 'Thank you for choosing us, here is your ticket.'
        html_message = render_to_string(
            'email_format.html', {'message': message, 'booking_obj': booking_obj})
        plain_message = strip_tags(html_message)
        from_email = 'pravasltd74@gmail.com'
        recipient_list = [request.user.email]
        send_mail(subject, plain_message, from_email,
                  recipient_list, html_message=html_message)
        return redirect("pravas:home")
    return redirect("pravas:ticket_booking")
