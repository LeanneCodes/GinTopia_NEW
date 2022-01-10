import json
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from .models import Reservation
from .forms import ReservationForm


def index(request):
    return render(request, 'reservations/index.html')


def booking_form(request):
    submitted = False
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/booking_form?submitted=True')
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
    return render_template("reservations/all_about_gin.html", gin=data)


def contact_us(request):
    return render(request, 'reservations/contact_us.html')


def sign_up(request):
    return render(request, 'account/sign_up.html')


class ReservationView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'booking_form.html'

