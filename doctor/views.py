from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import (
    MedicinePrescription,
    PatientHealth,
)

from .serializers import (
    MedicinePrescriptionAddSerializer,
    MedicinePrescriptionSerializer,
    PatientHealthSerializer,
)


# Create your views here.
class MedicinePrescriptionsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        appointment_id = request.GET.get("appointment")
        if appointment_id:
            medicine_prescription = MedicinePrescription.objects.filter(
                appointment_id=appointment_id
            )
        else:
            medicine_prescription = MedicinePrescription.objects.all()
        serializer = MedicinePrescriptionSerializer(medicine_prescription, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MedicinePrescriptionAddSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicinePrescriptionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        medicine_prescription = get_object_or_404(MedicinePrescription, pk=id)
        serializer = MedicinePrescriptionSerializer(medicine_prescription)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        medicine_prescription = get_object_or_404(MedicinePrescription, pk=id)
        serializer = MedicinePrescriptionAddSerializer(
            medicine_prescription, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        medicine_prescription = get_object_or_404(MedicinePrescription, pk=id)
        medicine_prescription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PatientHealthsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        patient_id = request.GET.get("patient")
        if patient_id:
            patient_health = PatientHealth.objects.filter(patient_id=patient_id)
        else:
            patient_health = PatientHealth.objects.all()
        serializer = PatientHealthSerializer(patient_health, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PatientHealthSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientHealthView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        patient_health = get_object_or_404(PatientHealth, pk=id)
        serializer = PatientHealthSerializer(patient_health)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        patient_health = get_object_or_404(PatientHealth, pk=id)
        serializer = PatientHealthSerializer(patient_health, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        patient_health = get_object_or_404(PatientHealth, pk=id)
        patient_health.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
