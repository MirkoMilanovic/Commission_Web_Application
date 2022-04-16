from django.db import models


class Reservation(models.Model):
    reservation_code = models.CharField(max_length=150,unique=True)
    checkin = models.DateField()
    checkout = models.DateField()
    flat = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    net_income = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.reservation_code
