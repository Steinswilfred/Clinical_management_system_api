from django.contrib import admin

from .models import (
    BloodGroup,
    ClinicInfo,
    # Designation,
    Doctor,
    Patient,
    Role,
    Specialization,
    Staff,
)

# Register your models here.
admin.site.register(BloodGroup)
admin.site.register(ClinicInfo)
# admin.site.register(Designation)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Role)
admin.site.register(Specialization)
admin.site.register(Staff)