import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from .models import Reservation
from .forms import ReservationForm


def index(request):
    return render(request, 'reservations/index.html')


def show_booking(request):
    items = Reservation.objects.all()
    context = {
        'items': items
    }

    return render(request, 'reservations/show_booking.html', context)


def booking_form(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_booking')
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
            return redirect('show_booking')
    form = ReservationForm
    context = {
        'form': form,
    }

    return render(request, 'reservations/update_booking.html', context)


def delete_booking(request, item_id):
    schedule = get_object_or_404(Reservation, id=item_id)
    schedule.delete()
    return redirect('show_booking')


# def form_filter_view(request):
#     items = Reservation.objects.all()
#     queryset = items
#     email_exact_query = request.GET.get('user_email')
#     if email_exact_query != '' and email_exact_query is not None:
#         queryset = queryset.filter(user_email__iexact=email_exact_query)

#     context = {
#         'queryset': queryset
#     }
#     return render(request, 'reservations/show_booking.html', context)


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


