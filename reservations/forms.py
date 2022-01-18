from django import forms
from django.forms import ModelForm
from .models import Reservation


# The fields available to iterate through in the user interface
class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'user_email', 'user_phone',
                  'date', 'time', 'for_how_many', 'mixologist']
