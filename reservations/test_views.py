from django.test import TestCase
from .models import Reservation
from django.shortcuts import render, redirect, get_object_or_404


class TestViews(TestCase):

    def test_get_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations/index.html')

    def test_get_all_about_gin(self):
        response = self.client.get('/all_about_gin')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations/all_about_gin.html')

    def test_book_a_class(self):
        response = self.client.get('/booking_form')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations/booking_form.html')

    def test_contact_us(self):
        response = self.client.get('/contact_us')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations/contact_us.html')
