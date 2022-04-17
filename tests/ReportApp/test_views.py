from django.test import TestCase, Client
from django.urls import reverse
from ReportApp.models import Reservation
from django.db import models
from django.db.models import Sum, F, CharField, Value
from django.db.models.functions import Concat


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.upload_url = reverse('upload')
        self.report_url = reverse('report')
        self.city_commission_url = reverse('city_commission')

        self.reservation1 = Reservation.objects.create(
            reservation_code = 'HMBXXXX',
            checkin = '2022-01-01',
            checkout = '2022-01-11',
            flat = 'Flat1',
            city = 'LONDON',
            net_income = 1000,
        )
        self.reservation2 = Reservation.objects.create(
            reservation_code = 'HMBXXX2',
            checkin = '2022-01-01',
            checkout = '2022-02-01',
            flat = 'Flat2',
            city = 'PARIS',
            net_income = 2000,
        )
        self.reservation2 = Reservation.objects.create(
            reservation_code = 'HMBXXX3',
            checkin = '2022-02-01',
            checkout = '2022-03-01',
            flat = 'Flat2',
            city = 'PORTO',
            net_income = 3000,
        )
        self.COMMISSION_RATES = {
            'LONDON': 10,
            'PARIS': 20,
            'PORTO': 10,
        }
        self.COMMISSION_PER_MONTH = {
            2: 2222,
            3: 3333,
            4: 4444,
        }


    def test_upload_GET(self):
        response = self.client.get(self.upload_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReportApp/upload.html')

    
    def test_upload_POST_csv(self):
        with open('Reservations.csv', 'rb') as csv:
            response = self.client.post(self.upload_url, data={'file': csv})
            self.assertRedirects(response, '/report', status_code=302, 
            target_status_code=200, fetch_redirect_response=True)


    def test_upload_POST_no_file(self):
        response = self.client.post(self.upload_url, {})

        self.assertRedirects(response, '/error_upload', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)


    def test_report_GET_total_commission(self):

        total_commission = 0

        for city in self.COMMISSION_RATES.keys():
            total_commission += Reservation.objects.filter(city=city).aggregate(result = Sum((F('net_income') * self.COMMISSION_RATES.get(city) / 100), output_field = models.DecimalField(max_digits=10, decimal_places=2)))['result']

        self.assertEquals(total_commission, 800)


    def test_report_GET_commission_per_month(self):

        query_list_commission = []
        
        month = 2

        query_list_commission.append(Reservation.objects.filter(checkout__month=month).annotate(monthly=Concat('checkout__year', Value('-'), 'checkout__month', Value(' -> '), self.COMMISSION_PER_MONTH.get(month), output_field=CharField(max_length=150))))

        results = Reservation.objects.none().union(*query_list_commission)

        for result in results:
            commission_per_month = result.monthly

        self.assertEquals(len(query_list_commission), 1)
        self.assertEquals(commission_per_month, '2022-2 -> 2222')


    def test_city_commission_GET(self):
        response = self.client.get(self.city_commission_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ReportApp/city_commission.html')


    def test_city_commission_POST_commission_amount_city(self):
        response = self.client.get(self.city_commission_url)

        city = 'LONDON'
        commission_amount_city = Reservation.objects.filter(city=city).aggregate(result = Sum((F('net_income') * self.COMMISSION_RATES[city] / 100), output_field = models.DecimalField(max_digits=10, decimal_places=2)))['result']

        self.assertEquals(response.status_code, 200)
        self.assertEquals(commission_amount_city, 100)
