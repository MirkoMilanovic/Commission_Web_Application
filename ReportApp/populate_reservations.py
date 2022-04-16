from .models import Reservation
import csv, io


def populateReservations(request):
    csv_file = request.FILES['file']
    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)

    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _ = Reservation.objects.update_or_create(
            reservation_code=column[0],
            checkin=column[1],
            checkout=column[2],
            flat=column[3],
            city=column[4],
            net_income=column[5],
        )