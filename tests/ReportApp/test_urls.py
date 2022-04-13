from django.urls import reverse, resolve
from ReportApp.views import upload, report, city_commission


def test_upload_url():
    path = reverse('upload')
    assert resolve(path).func == upload


def test_report_url():
    path = reverse('report')
    assert resolve(path).func == report


def test_city_commission_url():
    path = reverse('city_commission')
    assert resolve(path).func == city_commission


