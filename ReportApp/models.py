from django.db import models

# Create your models here.
class Reservations(models.Model):
    reservation = models.CharField(max_length=150,unique=True)
    checkin = models.DateField()
    checkout = models.DateField()
    flat = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    net_income = models.FloatField()
    
    def __str__(self):
        return self.reservation