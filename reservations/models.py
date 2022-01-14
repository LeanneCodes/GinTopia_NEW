from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Mixologist(models.Model):
    first_name = models.CharField(primary_key=True, max_length=30)
    last_name = models.CharField(max_length=30)
    user_phone = models.CharField(max_length=11)

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        return self.first_name


class Reservation(models.Model):
    user = models.ForeignKey(User, default='', null=True,
                             on_delete=models.CASCADE, related_name='hiuser')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=254)
    user_phone = models.CharField(max_length=11)
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    for_how_many = models.IntegerField(blank=False)
    mixologist = models.ForeignKey(
        'Mixologist', null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=False)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.user_email
