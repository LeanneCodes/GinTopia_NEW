from django.contrib import admin
from .models import Mixologist, Reservation


@admin.register(Mixologist)
class MixologistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_phone')
    search_fields = ['first_name', 'last_name', 'user_phone']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('mixologist',)}
    list_filter = ('status', 'date')
    list_display = ('mixologist', 'user_email', 'first_name',
                    'last_name', 'status', 'date')
    search_fields = ['status', 'date', 'time']
