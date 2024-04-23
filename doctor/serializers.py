from rest_framework import serializers
from cms_admin.models import Patient
from pharmacist.models import Medicince
from receptionist.models import Appointment

from cms_admin.serializers import PatientIdSerializer, PatientSerializer
from pharmacist.serializers import MedicineIdSerializer, MedicineSerializer
from receptionist.serializers import AppointmentIdSerializer, AppointmentSerializer

from .models import (
    MedicinePrescription,
    PatientHealth,
)


class MedicinePrescriptionSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer()
    patient = PatientSerializer()
    medicine = MedicineSerializer()

    class Meta:
        model = MedicinePrescription
        fields = "__all__"


class MedicinePrescriptionAddSerializer(serializers.ModelSerializer):
    appointment = AppointmentIdSerializer()
    patient = PatientIdSerializer()
    medicine = MedicineIdSerializer()

    class Meta:
        model = MedicinePrescription
        fields = "__all__"

    def create(self, validated_data):
        appointment_id = validated_data.pop("appointment")
        patient_id = validated_data.pop("patient")
        medicine_id = validated_data.pop("medicine")

        medicine_prescription = MedicinePrescription.objects.create(
            **validated_data,
            appointment_id=appointment_id,
            patient_id=patient_id,
            medicine_id=medicine_id,
        )

        return medicine_prescription

    def update(self, instance, validated_data):
        medicine_prescription = instance
        medicine_prescription.appointment_id = validated_data.get(
            "appointment", medicine_prescription.appointment_id
        )
        medicine_prescription.medicine_id = validated_data.get(
            "medicine", medicine_prescription.medicine_id
        )
        medicine_prescription.dosage = validated_data.get(
            "dosage", medicine_prescription.dosage
        )
        medicine_prescription.no_of_days = validated_data.get(
            "no_of_days", medicine_prescription.no_of_days
        )
        medicine_prescription.quantity = validated_data.get(
            "quantity", medicine_prescription.quantity
        )

        medicine_prescription.save()

        return medicine_prescription

    def validate_appointment(self, value):
        appointment_id = value.get("id")
        if not Appointment.objects.filter(id=appointment_id).exists():
            raise serializers.ValidationError("Appointment Doesn't Exist")
        return appointment_id

    def validate_patient(self, value):
        patient_id = value.get("id")
        if not Patient.objects.filter(id=patient_id).exists():
            raise serializers.ValidationError("Patient Doesn't Exist")
        return patient_id

    def validate_medicine(self, value):
        medicine_id = value.get("id")
        if not Medicince.objects.filter(id=medicine_id).exists():
            raise serializers.ValidationError("Medicine Doesn't Exist")
        return medicine_id


class PatientHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHealth
        fields = "__all__"
