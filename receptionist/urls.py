from django.urls import path
from .views import appointment_list,appointment_add,appointment_edit,appointment_bill, appointment

urlpatterns = [
    path('api/appointments/', appointment_list),
    path('api/appointment/<int:id>', appointment),
    path('api/appointments/add', appointment_add),
    path('api/appointments/edit/<int:id>', appointment_edit),
    path('api/appointments_bill', appointment_bill)
]
