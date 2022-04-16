from datetime import date
from django.test import TestCase
from ReportApp.models import Reservation


class TestModels(TestCase):
    def setUp(self):
        self.reservation1 = Reservation.objects.create(
            reservation_code = 'Reservation1',
            checkin = date(22, 1, 1),
            checkout = date(22, 2, 2),
            flat = 'Flat1',
            city = 'City1',
            net_income = 1000
        )


    def test_reservation(self):
        self.assertEquals(self.reservation1.net_income, 1000)
