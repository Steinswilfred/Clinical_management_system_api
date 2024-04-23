from django.contrib import admin

from .models import MedicinePrescription, PatientHealth

# Register your models here.
admin.site.register(MedicinePrescription)
admin.site.register(PatientHealth)
