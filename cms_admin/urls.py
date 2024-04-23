from django.urls import path

from .views import (
    BloodGroupsView,
    BloodGroupView,
    ClinicInfosView,
    ClinicInfoView,
    DesignationsView,
    DesignationView,
    DoctorsView,
    DoctorView,
    PatientsView,
    PatientView,
    RolesView,
    RoleView,
    SpecializationsView,
    SpecializationView,
    UsersView,
    StaffsView,
    StaffView,
)

urlpatterns = [
    path("api/cms_admin/blood-group/<int:id>", BloodGroupView.as_view()),
    path("api/cms_admin/blood-groups", BloodGroupsView.as_view()),
    path("api/cms_admin/clinic-info/<int:id>", ClinicInfoView.as_view()),
    path("api/cms_admin/clinic-infos", ClinicInfosView.as_view()),
    path("api/cms_admin/designation/<int:id>", DesignationView.as_view()),
    path("api/cms_admin/designations", DesignationsView.as_view()),
    path("api/cms_admin/doctor/<int:id>", DoctorView.as_view()),
    path("api/cms_admin/doctors", DoctorsView.as_view()),
    path("api/cms_admin/patient/<int:id>", PatientView.as_view()),
    path("api/cms_admin/patients", PatientsView.as_view()),
    path("api/cms_admin/role/<int:id>", RoleView.as_view()),
    path("api/cms_admin/roles", RolesView.as_view()),
    path("api/cms_admin/specialization/<int:id>", SpecializationView.as_view()),
    path("api/cms_admin/specializations", SpecializationsView.as_view()),
    path("api/cms_admin/users", UsersView.as_view()),
    path("api/cms_admin/staff/<int:id>", StaffView.as_view()),
    path("api/cms_admin/staffs", StaffsView.as_view()),

]
