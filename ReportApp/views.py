from django.shortcuts import render, redirect
from django.views import View
from .models import Reservation
from .forms import RatesForm
from .populate_reservations import populateReservations
from django.contrib import messages
from django.db.models import Sum
from .constants import COMMISSION_RATES, COMMISSION_PER_MONTH


class UploadView(View):
    def get(self, request):
        template = "ReportApp/upload.html"
        return render(request, template)

    def post(self, request):
        try:
            populateReservations(request)

            messages.success(request, 'Upload is successful. Data saved to DB.')

            return redirect(report_view)
        except:
            return redirect(error_upload_view)


class ReportView(View):
    def get(self, request):
        try:
            reservations_table = Reservation.objects.all()
 
            total_commission = 0

            for reservation in reservations_table:
                for city in COMMISSION_RATES.keys():
                    if reservation.city == city.upper():
                        total_commission += reservation.net_income * COMMISSION_RATES[city] / 100

            for reservation in reservations_table:
                for month in COMMISSION_PER_MONTH:
                    if reservation.checkout.month == month:
                        reservation.monthly = COMMISSION_PER_MONTH[month]


            report_context = {
                'reports': reservations_table,
                'total': total_commission,
            }

            return render(request, 'ReportApp/report.html', report_context)
        except:
            return redirect(error_report_view)


class CityCommissionView(View):
    def get(self, request):
        form = RatesForm()
        commission_amount_city = 0
        rate_context = {
            'form': form, 
            'commission_amount_city': commission_amount_city
        }
        return render(request, 'ReportApp/city_commission.html', rate_context)

    def post(self, request):
        commission_amount_city = 0

        form = RatesForm(request.POST)
        
        if form.is_valid():
            commission_amount_city = Reservation.objects.filter(city=form.cleaned_data["city"]).aggregate(sum_net = Sum('net_income'))['sum_net']*COMMISSION_RATES[form.cleaned_data['city']] / 100

        rate_context = {
            'form': form, 
            'commission_amount_city': commission_amount_city
        }
        return render(request, 'ReportApp/city_commission.html', rate_context)


class ErrorUploadView(View):
    def get(self, request):
        return render(request, 'ReportApp/error_upload.html')


class ErrorReportView(View):
    def get(self, request):
        return render(request, 'ReportApp/error_report.html')


upload_view = UploadView.as_view()
report_view = ReportView.as_view()
city_commission_view = CityCommissionView.as_view()
error_upload_view = ErrorUploadView.as_view()
error_report_view = ErrorReportView.as_view()