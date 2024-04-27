from django.urls import path

from .views import (
    MedicinePrescriptionsView,
    MedicinePrescriptionView,
    PatientHealthsView,
    PatientHealthView,
)

urlpatterns = [
    path("api/doctor/medicine-prescriptions/", MedicinePrescriptionsView.as_view()),
    path("api/doctor/medicine-prescription/<int:id>", MedicinePrescriptionView.as_view()),
    path("api/doctor/patient-healths/", PatientHealthsView.as_view()),
    path("api/doctor/patient-health/<int:id>", PatientHealthView.as_view())
]
