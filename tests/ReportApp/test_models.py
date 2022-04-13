import pytest
from datetime import date
from ReportApp.models import Reservations


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

def test_filter_category(category):
    assert Reservations.objects.filter(reservation="Reservation 1").exists()
    assert Reservations.objects.filter(checkin = date(22, 1, 1)).exists()
    assert Reservations.objects.filter(checkout = date(22, 2, 2)).exists()
    assert Reservations.objects.filter(flat = 'Flat 1').exists()
    assert Reservations.objects.filter(city = 'City 1').exists()
    assert Reservations.objects.filter(net_income = 1000).exists()


def test_update_category(category):
    category.reservation = "Reservation 2"
    category.save()
    category_from_db = Reservations.objects.get(reservation="Reservation 2")
    assert category_from_db.reservation == "Reservation 2"