import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from .models import Reservation
from .forms import ReservationForm


def index(request):
    return render(request, 'reservations/index.html')


def update_booking(request):
    items = Reservation.objects.all()
    context = {
        'items': items
    }
    return render(request, 'reservations/update_booking.html', context)


def booking_form(request):
    submitted = False
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('update_booking')
    else :
        form = ReservationForm
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form': form,
        'submitted': submitted
    }
    return render(request, 'reservations/booking_form.html', context)


def all_about_gin(request):
    return render(request, 'reservations/all_about_gin.html')


def all_about_gin(request):
    data = []
    with open("data/gin.json", "r") as json_data:
        data = json.load(json_data)

    context = {
        'data': data
    }

    return render(request, "reservations/all_about_gin.html", context)


def contact_us(request):
    return render(request, 'reservations/contact_us.html')


def sign_up(request):
    return render(request, 'account/sign_up.html')


