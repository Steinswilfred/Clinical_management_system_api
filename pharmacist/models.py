from django.db import models

from receptionist.models import Appointment

# Create your models here.


class Medistate(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Medicince(models.Model):
    medicince_name=models.CharField(max_length=25)
    genericName=models.CharField(max_length=20)
    companyName=models.CharField(max_length=15)
    quantity=models.PositiveIntegerField()
    rate=models.DecimalField(max_digits=10,decimal_places=3)
    state=models.ForeignKey(Medistate,on_delete=models.CASCADE)
    expiration_date=models.DateField()
    is_active = models.BooleanField(default=True)
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return self.medicince_name


class MedicinePrescriptionBill(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicince, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.appointment.patient} {self.medicine}"