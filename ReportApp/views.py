from django.shortcuts import render, redirect
import csv, io
from django.contrib import messages
from .models import Reservations
from . import forms


commission_rates = {
    'LONDON': 10,
    'PARIS': 12,
    'PORTO': 9,
}

commission_per_month = {
    5: 977.1,   # May
    6: 1684,    # June
}

# Create your views here.
def upload(request):
    try:
        Reservations.objects.all().delete()     # Delete previous list of reservations

        template = "ReportApp/upload.html"

        # GET request returns the value of the data with the specified key
        if request.method == "GET":
            return render(request, template)
        csv_file = request.FILES['file']

        data_set = csv_file.read().decode('UTF-8')
        # setup a stream which is when we loop through each line we are able to handle a data in a stream
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = Reservations.objects.update_or_create(
                reservation=column[0],
                checkin=column[1],
                checkout=column[2],
                flat=column[3],
                city=column[4],
                net_income=column[5],
            )
        return redirect('report')
    except:
        return redirect('error')


def report(request):
    try:
        reservations_table = Reservations.objects.all()

        total_commission = 0

        for reservation in reservations_table:
            for city in commission_rates.keys():
                if reservation.city == city.upper():
                    total_commission += reservation.net_income * commission_rates[city] / 100


        for reservation in reservations_table:
            for month in commission_per_month:
                if reservation.checkout.month == month:
                    reservation.monthly = commission_per_month[month]

        report_context = {
            'reports': reservations_table,
            'total': total_commission,
        }

        return render(request, 'ReportApp/report.html', report_context)
    except:
        return redirect('error')


def city_commission(request):
    form = forms.RatesForm()
    commission_amount_city = 0

    if request.method == 'POST':
        form = forms.RatesForm(request.POST)
        

        if form.is_valid():
            reservations_table_city = Reservations.objects.filter(city=form.cleaned_data["rates"])

            for reservation in reservations_table_city:
                commission_amount_city += reservation.net_income * commission_rates[form.cleaned_data['rates']] / 100
            
            print(commission_amount_city)

    rate_context = {
        'form': form, 
        'commission_amount_city': commission_amount_city
    }

    return render(request, 'ReportApp/city_commission.html', rate_context)


def error(request):
    return render(request, 'ReportApp/error.html')