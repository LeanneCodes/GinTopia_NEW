from django.test import TestCase
from .forms import ReservationForm


class TestReservationForm(TestCase):
    def test_reservation_name_is_required(self):
        form = ReservationForm({"first_name": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["first_name"][0], "This field is required.")

    def test_for_how_many_field_is_not_required(self):
        form = ReservationForm({"for_how_many": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("for_how_many", form.errors.keys())
        self.assertEqual(form.errors["for_how_many"][0], "This field is required.")

    def test_slug_is_not_required(self):
        form = ReservationForm({"first_name": "Test Reservation"})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ReservationForm()
        self.assertEqual(
            form.Meta.fields,
            [
                "first_name",
                "last_name",
                "user_email",
                "user_phone",
                "date",
                "time",
                "for_how_many",
                "mixologist",
            ],
        )
