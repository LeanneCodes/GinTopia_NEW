"""gintopia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reservations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('booking_form', views.booking_form, name='booking_form'),
    path('show_booking', views.show_booking, name='show_booking'),
    path('update/<item_id>', views.update_booking, name='update_booking'),
    path('delete/<item_id>', views.delete_booking,
         name='delete_booking'),
    path('all_about_gin', views.all_about_gin, name='all_about_gin'),
    path('contact_us', views.contact_us, name='contact_us'),
    path("accounts/", include("allauth.urls")),
]
