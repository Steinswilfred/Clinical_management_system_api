from rest_framework import serializers

from cms_admin.models import Patient
from cms_admin.serializers import PatientIdSerializer, PatientSerializer
from receptionist.models import Appointment
from receptionist.serializers import AppointmentSerializer, AppointmentIdSerializer

from .models import LabTest,LabTestReport
from cms_admin.models import Patient
class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTest
        fields = "__all__"

class LabTestIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = LabTest
        fields = ("id",)

    def validate_id(self, value):
        return value

class LabTestReportSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer()
    patient = PatientSerializer()
    test_type = LabTestSerializer()

    class Meta:
        model = LabTestReport
        fields = "__all__"

class LabTestReportAddSerializer(serializers.ModelSerializer):
    appointment = AppointmentIdSerializer()
    patient = PatientIdSerializer()
    test_type = LabTestIdSerializer()

    class Meta:
        model = LabTestReport
        fields = "__all__"

    def create(self, validated_data):
        appointment_id = validated_data.pop("appointment")
        patient_id = validated_data.pop("patient")
        test_type_id = validated_data.pop("test_type")

        test_report = LabTestReport.objects.create(**validated_data, appointment_id=appointment_id, patient_id=patient_id, test_type_id=test_type_id)
        return test_report
    
    def update(self, instance, validated_data):
        test_report = instance
        test_report.test_type_id = validated_data.get("test_type", test_report.test_type_id)
        test_report.result = validated_data.get("result", test_report.result)
        test_report.report = validated_data.get("report", test_report.report)
        test_report.save()
        
        return test_report
    
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
    
    def validate_test_type(self, value):
        test_id = value.get("id")
        if not LabTest.objects.filter(id=test_id).exists():
            raise serializers.ValidationError("Test Doesn't Exist")
        return test_id