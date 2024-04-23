from datetime import datetime

from rest_framework import serializers
from cms_admin.models import Patient, Doctor
from cms_admin.serializers import (
    DoctorIdSerializer,
    DoctorSerializer,
    PatientIdSerializer,
    PatientSerializer,
)

from .models import Appointment, Appointment_Bill


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    patient = PatientSerializer()

    class Meta:
        model = Appointment
        fields = "__all__"

class AppointmentIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Appointment
        fields = ("id",)
    
    def validate_id(self, value):
        return value


class AppointmentAddSerializer(serializers.ModelSerializer):
    patient = PatientIdSerializer()
    doctor = DoctorIdSerializer()

    class Meta:
        model = Appointment
        fields = "__all__"

    def create(self, validated_data):
        patient_id = validated_data.pop("patient")
        doctor_id = validated_data.pop("doctor")

        appointment = Appointment.objects.create(
            **validated_data, patient_id=patient_id, doctor_id=doctor_id
        )

        return appointment

    def update(self, instance, validated_data):
        appointment = instance
        appointment.patient_id = validated_data.get("patient", instance.patient)
        appointment.doctor_id = validated_data.get("doctor", instance.doctor)
        appointment.appointment_time = validated_data.get(
            "appointment_time", datetime.now()
        )
        appointment.is_done = validated_data.get("is_done", instance.is_done)
        appointment.save()

        return appointment

    def validate_patient(self, value):
        patient_id = value.get("id")
        if not Patient.objects.filter(id=patient_id).exists():
            raise serializers.ValidationError("Patient Doesn't Exist")
        return patient_id

    def validate_doctor(self, value):
        doctor_id = value.get("id")
        if not Doctor.objects.filter(id=doctor_id).exists():
            raise serializers.ValidationError("Doctor Doesn't Exist")
        return doctor_id


class AppointmentBillSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer()

    class Meta:
        model = Appointment_Bill
        fields = "__all__"
