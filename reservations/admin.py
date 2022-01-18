from django.contrib import admin
from .models import Mixologist, Reservation


# admin view of the Mixologist model in the Django Administration
@admin.register(Mixologist)
class MixologistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_phone')
    search_fields = ['first_name', 'last_name', 'user_phone']


# admin view of the Reservation model in the Django Administration
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('mixologist',)}
    list_filter = ('date', 'mixologist')
    list_display = ('mixologist', 'user_email', 'first_name',
                    'last_name', 'date', 'time')
    search_fields = ['date', 'time']
