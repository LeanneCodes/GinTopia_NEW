import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm


# Homepage view
def index(request):
    return render(request, 'reservations/index.html')


# Show logged in users their current bookings, if they have any
def show_booking(request):
    items = request.user.hiuser.all()
    context = {
        'items': items
    }

    return render(request, 'reservations/show_booking.html', context)


# Show logged in users the booking form to create their booking
def booking_form(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Your booking was created successfully!')
            return redirect('show_booking')
        else:
            messages.warning(request,
                             'Booking not successful. '
                             'Check date chosen is not in the past. '
                             'Please ensure all fields have valid inputs.')
            return redirect('booking_form')
    else:
        form = ReservationForm
        context = {
            'form': form,
        }

    return render(request, 'reservations/booking_form.html', context)


# Give logged in users the opportunity to update their bookings
# and be redirected to other bookings they may have
def update_booking(request, item_id):
    schedule = get_object_or_404(Reservation, id=item_id)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking was updated successfully!')
            return redirect('show_booking')
        else:
            messages.warning(request, 'Booking was not updated. '
                             'Check date chosen is not in the past. '
                             'Please ensure all fields have valid inputs.')
    form = ReservationForm
    context = {
        'form': form,
    }

    return render(request, 'reservations/update_booking.html', context)


# Logged in users can delete their booking and be redirected
# to other bookings they may have
def delete_booking(request, item_id):
    schedule = get_object_or_404(Reservation, id=item_id)
    if schedule.delete():
        messages.success(request, 'Your booking was deleted successfully!')
        return redirect('show_booking')
    else:
        messages.warning(request, 'Booking was not deleted.')


# All About Gin page view
# The gin.json file that populates the top 10 gin bottles and a
# description of the bottles on the All About Gin page
def all_about_gin(request):
    data = []
    with open("data/gin.json", "r") as json_data:
        data = json.load(json_data)

    context = {
        'data': data
    }

    return render(request, "reservations/all_about_gin.html", context)


# The Contact Us page view
def contact_us(request):
    return render(request, 'reservations/contact_us.html')
