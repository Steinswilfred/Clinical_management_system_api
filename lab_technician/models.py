from django.db import models

from cms_admin.models import Patient
from receptionist.models import Appointment

class LabTest(models.Model):
    test_name = models.CharField(max_length=50,blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return self.test_name

class LabTestReport(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=False)
    test_type = models.ForeignKey(LabTest,on_delete=models.CASCADE)
    result = models.BooleanField(default=False)
    report = models.TextField(blank=True)

    def __str__(self):
        return f"Report for {self.patient} - Test: {self.test_type.test_name}, Result: {self.result}"