import datetime
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Mixologist model created, so if a mixologist is no longer
# available to work, bookings made with them will be cancelled
class Mixologist(models.Model):
    first_name = models.CharField(primary_key=True, max_length=30)
    last_name = models.CharField(max_length=30)
    user_phone = models.CharField(max_length=11)

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        return self.first_name


# Reservation model created, so the admin can collect details
# from the user during the booking process, which can help
# facilitate with the event on the day.
class Reservation(models.Model):
    TIMES = [
        ("13:00", "13:00"),
        ("15:00", "15:00"),
        ("17:00", "17:00"),
        ("19:00", "19:00"),
        ("21:00", "21:00")
    ]

    PEOPLE = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10")
    ]

    GENDER = [
        ("Woman", "Woman"),
        ("Man", "Man"),
        ("Other", "Other")
    ]

    user = models.ForeignKey(User, default='', null=True,
                             on_delete=models.CASCADE, related_name='hiuser')
    first_name = models.CharField(max_length=30)
    age = models.IntegerField(blank=False, null=False)
    gender = models.CharField(max_length=6, choices=GENDER)
    last_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=254)
    user_phone = models.CharField(max_length=11)
    date = models.DateField(max_length=10, validators=[MinValueValidator(
                            datetime.date.today)])
    time = models.CharField(max_length=5, choices=TIMES)
    for_how_many = models.CharField(max_length=6, choices=PEOPLE)
    mixologist = models.ForeignKey('Mixologist', null=True,
                                   on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique=False)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.user_email
