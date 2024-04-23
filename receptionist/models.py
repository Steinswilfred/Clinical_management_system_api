from django.db import models

from cms_admin.models import Patient, Doctor

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField(auto_now_add= True)
    is_done = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.patient} {self.doctor}"


class Appointment_Bill(models.Model):
    bill_amount = models.PositiveSmallIntegerField()
    fee_name = models.CharField(max_length=50)
    bill_time = models.DateTimeField(auto_now_add=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.appointment.patient} {self.bill_amount}"
