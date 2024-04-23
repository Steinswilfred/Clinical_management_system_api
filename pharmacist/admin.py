from django.contrib import admin
from django.contrib.admin import site

from pharmacist.models import Medicince, Medistate, MedicinePrescriptionBill

# Register your models here.
admin,site.register(Medicince)
admin,site.register(Medistate)
admin,site.register(MedicinePrescriptionBill)
