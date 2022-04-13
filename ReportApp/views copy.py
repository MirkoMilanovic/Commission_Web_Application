from django.shortcuts import render
from django.http import HttpResponse
import csv, io
from django.contrib import messages
from .models import Reservations


# Create your views here.
def index(request):
    return HttpResponse('Mirko')


# one parameter named request
def upload(request):
    # declaring template
    template = "ReportApp/render.html"
    data = Reservations.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be: reservation, checkin, checkupt, flat, city, net income',
        'reservationsfiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE!')
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
    context = {}
    return render(request, template, context)
