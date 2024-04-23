from django.db import models

from cms_admin.models import Patient
from receptionist.models import Appointment
from pharmacist.models import Medicince


# Create your models here.
class MedicinePrescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicince, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    dosage = models.PositiveSmallIntegerField()
    no_of_days = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.patient} {self.medicine}"


class PatientHealth(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    blood_pressure = models.CharField(max_length=10)
    sugar_level = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    diagnosis = models.CharField(max_length=250)
    note = models.TextField()

    def __str__(self):
        return f"{self.patient} {self.diagnosis}"
