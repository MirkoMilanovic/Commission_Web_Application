from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ReportApp.views import UploadView, ReportView, CityCommissionView, ErrorReportView, ErrorUploadView


class TestUrls(SimpleTestCase):

    def test_list_url_upload(self):
        url = reverse('upload')
        self.assertEquals(resolve(url).func.view_class, UploadView)


    def test_add_url_report(self):
        url = reverse('report')
        self.assertEquals(resolve(url).func.view_class, ReportView)


    def test_detail_url_city_commission(self):
        url = reverse('city_commission')
        self.assertEquals(resolve(url).func.view_class, CityCommissionView)

    
    def test_test_detail_url_city_commission_url_error_upload(self):
        url = reverse('error_upload')
        self.assertEquals(resolve(url).func.view_class, ErrorUploadView)


    def test_test_detail_url_city_commission_url_error_report(self):
        url = reverse('error_report')
        self.assertEquals(resolve(url).func.view_class, ErrorReportView)