import pytest

from django.test import RequestFactory, Client
from django.urls import reverse
from ReportApp.models import Reservations
from datetime import date
from ReportApp.views import upload, report, city_commission

@pytest.fixture
def category(db) -> Reservations:
    return Reservations.objects.create(
        reservation="Reservation 1",  
        checkin = date(22, 1, 1),
        checkout = date(22, 2, 2),
        flat = 'Flat 1',
        city = 'City 1',
        net_income = 1000
    )

reservation = {
    'reservation':"Reservation 2",  
    'checkin' : date(22, 1, 1),
    'checkout' : date(22, 2, 2),
    'flat' : 'Flat 1',
    'city' : 'City 1',
    'net_income' : 1000 
}

def test_1(category):
    factory = RequestFactory()
    request = factory.get('/upload')
    response = upload(request)
    assert response.status_code == 200


def test_redirection_upload():
    c = Client()

    response = c.get(reverse('upload'), reservation)

    assert response.status_code == 302


def test_redirection_report():
    c = Client()

    response = c.get(reverse('report'))

    assert response.status_code == 302
