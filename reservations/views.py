import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm


def index(request):
    return render(request, 'reservations/index.html')


def show_booking(request):
    items = request.user.hiuser.all()
    context = {
        'items': items
    }

    return render(request, 'reservations/show_booking.html', context)


def booking_form(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Your booking was created successfully!')
            return redirect('show_booking')
        else:
            messages.warning(request, 'Please correct the error(s).')
    else: 
        form = ReservationForm
        context = {
            'form': form,
        }

    return render(request, 'reservations/booking_form.html', context)


def update_booking(request, item_id):
    schedule = get_object_or_404(Reservation, id=item_id)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking was updated successfully!')
            return redirect('show_booking')
        else:
            messages.warning(request, 'Please correct the error(s).')
    form = ReservationForm
    context = {
        'form': form,
    }

    return render(request, 'reservations/update_booking.html', context)


def delete_booking(request, item_id):
    schedule = get_object_or_404(Reservation, id=item_id)
    if schedule.delete():
        messages.success(request, 'Your booking was deleted successfully!')
        return redirect('show_booking')
    else:
        messages.warning(request, 'Please correct the error(s).')


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

