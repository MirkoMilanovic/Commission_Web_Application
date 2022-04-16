from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.upload_url = reverse('upload')
        self.report_url = reverse('report')
        self.city_commission_url = reverse('city_commission')
        


    def test_upload_GET(self):
        response = self.client.get(self.upload_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReportApp/upload.html')

    
    def test_upload_POST(self):
        with open('Reservations.csv', 'rb') as csv:
            response = self.client.post(self.upload_url, data={'file': csv})
            self.assertRedirects(response, '/report', status_code=302, 
            target_status_code=200, fetch_redirect_response=True)


    def test_upload_POST_empty(self):
        response = self.client.post(self.upload_url, {})

        self.assertRedirects(response, '/error_upload', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)


    def test_report_GET(self):
        response = self.client.get(self.report_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReportApp/report.html')


    def test_city_commission_GET(self):
        response = self.client.get(self.city_commission_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReportApp/city_commission.html')


