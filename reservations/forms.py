from django import forms
from django.forms import ModelForm
from .models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'user_email', 'user_phone',
                  'date', 'time', 'for_how_many', 'mixologist']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'user_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={
                'class': 'form-control', 'placeholder': 'YYYY/MM/DD'}),
            'time': forms.TextInput(attrs={'class': 'form-control'}),
            'for_how_many': forms.TextInput(attrs={'class': 'form-control'}),
            'mixologists': forms.Select(attrs={'class': 'form-control'}),
        }