from django.contrib import admin

from .models import Appointment, Appointment_Bill


# Register your models here.
admin.site.register(Appointment)
admin.site.register(Appointment_Bill)
