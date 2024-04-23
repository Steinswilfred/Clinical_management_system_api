from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
from .models import (
    BloodGroup,
    ClinicInfo,
    Designation,
    Doctor,
    Patient,
    Role,
    Specialization,
    Staff,
)

from .serializers import (
    BloodGroupSerializer,
    ClinicInfoSerializer,
    DesignationSerializer,
    DoctorAddSerializer,
    DoctorSerializer,
    PatientAddSerializer,
    PatientSerializer,
    RoleSerializer,
    SpecializationSerializer,
    StaffAddSerializer,
    StaffSerializer,
    UserSerializer,
)


class BloodGroupsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        blood_groups = BloodGroup.objects.all()
        serializer = BloodGroupSerializer(blood_groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BloodGroupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BloodGroupView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        blood_group = get_object_or_404(BloodGroup, pk=id)
        serializer = BloodGroupSerializer(blood_group)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        blood_group = get_object_or_404(BloodGroup, pk=id)
        serializer = BloodGroupSerializer(instance=blood_group, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        blood_group = get_object_or_404(BloodGroup, pk=id)
        blood_group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClinicInfosView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        clinic_infos = ClinicInfo.objects.all()
        serializer = ClinicInfoSerializer(clinic_infos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClinicInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClinicInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        clinic_info = get_object_or_404(ClinicInfo, pk=id)
        serializer = ClinicInfoSerializer(clinic_info)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        clinic_info = get_object_or_404(ClinicInfo, pk=id)
        serializer = ClinicInfoSerializer(instance=clinic_info, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        clinic_info = get_object_or_404(ClinicInfo, pk=id)
        clinic_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DesignationsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        designations = Designation.objects.all()
        serializer = DesignationSerializer(designations, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DesignationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DesignationView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        designation = get_object_or_404(Designation, pk=id)
        serializer = DesignationSerializer(designation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        designation = get_object_or_404(Designation, pk=id)
        serializer = DesignationSerializer(instance=designation, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        designation = get_object_or_404(Designation, pk=id)
        designation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DoctorsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        specialization_id = request.GET.get("specialization")
        if specialization_id:
            doctors = Doctor.objects.filter(specialization_id=specialization_id)
        else:
            doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DoctorAddSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        doctor = get_object_or_404(Doctor, pk=id)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        doctor = get_object_or_404(Doctor, pk=id)
        serializer = DoctorAddSerializer(
            instance=doctor, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        doctor = get_object_or_404(Doctor, pk=id)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UsersView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class StaffsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        staffs = Staff.objects.exclude(role__name="Doctor")
        serializer = StaffSerializer(staffs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StaffAddSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        staff = get_object_or_404(Staff, pk=id)
        serializer = StaffSerializer(staff)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        staff = get_object_or_404(Staff, pk=id)
        serializer = StaffAddSerializer(instance=staff, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        staff = get_object_or_404(Staff, pk=id)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpecializationsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        specializations = Specialization.objects.all()
        serializer = SpecializationSerializer(specializations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SpecializationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecializationView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        specialization = get_object_or_404(Specialization, pk=id)
        serializer = SpecializationSerializer(specialization)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        specialization = get_object_or_404(Specialization, pk=id)
        serializer = SpecializationSerializer(
            instance=specialization, data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        specialization = get_object_or_404(Specialization, pk=id)
        specialization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RolesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        roles = Role.objects.exclude(name="Doctor")
        serializer = RoleSerializer(roles, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        role = get_object_or_404(Role, pk=id)
        serializer = RoleSerializer(role)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        role = get_object_or_404(Role, pk=id)
        serializer = RoleSerializer(instance=role, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        role = get_object_or_404(Role, pk=id)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PatientsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PatientAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        patient = get_object_or_404(Patient, pk=id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        patient = get_object_or_404(Patient, pk=id)
        serializer = PatientAddSerializer(
            instance=patient, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        patient = get_object_or_404(Patient, pk=id)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

