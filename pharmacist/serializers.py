from rest_framework import serializers

from pharmacist.models import Medicince, MedicinePrescriptionBill, Medistate
from receptionist.models import Appointment
from receptionist.serializers import AppointmentIdSerializer, AppointmentSerializer


class MedicineStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medistate
        fields = "__all__"


class MedicineStateIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Medistate
        fields = ("id",)

    def validate_id(self, value):
        return value


class MedicineSerializer(serializers.ModelSerializer):
    state = MedicineStateSerializer()

    class Meta:
        model = Medicince
        fields = "__all__"


class MedicineIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Medicince
        fields = ("id",)

    def validate_id(self, value):
        return value


class MedicineAddSerializer(serializers.ModelSerializer):
    state = MedicineStateIdSerializer()

    class Meta:
        model = Medicince
        fields = "__all__"

    def create(self, validated_data):
        state_id = validated_data.pop("state")
        medicine = Medicince.objects.create(**validated_data, state_id=state_id)
        return medicine

    def update(self, instance, validated_data):
        medicine = instance
        medicine.medicince_name = validated_data.get(
            "medicince_name", medicine.medicince_name
        )
        medicine.genericName = validated_data.get("genericName", medicine.genericName)
        medicine.companyName = validated_data.get("companyName", medicine.companyName)
        medicine.quantity = validated_data.get("quantity", medicine.quantity)
        medicine.rate = validated_data.get("rate", medicine.rate)
        medicine.state_id = validated_data.get("state", medicine.state_id)
        medicine.expiration_date = validated_data.get(
            "expiration_date", medicine.expiration_date
        )
        medicine.is_enable = validated_data.get("is_enable", medicine.is_enable)
        medicine.is_active = validated_data.get("is_active", medicine.is_active)

        medicine.save()
        return medicine

    def validate_state(self, value):
        state_id = value.get("id")
        if not Medistate.objects.filter(id=state_id).exists():
            raise serializers.ValidationError("Medicine State Doesn't Exist")
        return state_id


class MedicinePrescriptionBillSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer()
    medicine = MedicineSerializer()

    class Meta:
        model = MedicinePrescriptionBill
        fields = "__all__"


class MedicinePrescriptionAddBillSerializer(serializers.ModelSerializer):
    appointment = AppointmentIdSerializer()
    medicine = MedicineIdSerializer()

    class Meta:
        model = MedicinePrescriptionBill
        fields = "__all__"

    def create(self, validated_data):
        appointment_id = validated_data.pop("appointment")
        medicine_id = validated_data.pop("medicine")
        quantity = validated_data.pop("quantity")

        medicine = Medicince.objects.get(id=medicine_id)

        medicine.quantity -= quantity
        medicine.save()

        medicine_prescription_bill = MedicinePrescriptionBill.objects.create(
            quantity=quantity,
            appointment_id=appointment_id,
            medicine_id=medicine_id,
        )

        return medicine_prescription_bill

    def update(self, instance, validated_data):
        medicine_prescription_bill = instance
        medicine_prescription_bill.appointment_id = validated_data.get(
            "appointment", medicine_prescription_bill.appointment_id
        )
        medicine_prescription_bill.medicine_id = validated_data.get(
            "medicine", medicine_prescription_bill.medicine_id
        )
        medicine_prescription_bill.quantity = validated_data.get(
            "quantity", medicine_prescription_bill.quantity
        )

        medicine_prescription_bill.save()

        return medicine_prescription_bill

    def validate_appointment(self, value):
        appointment_id = value.get("id")
        if not Appointment.objects.filter(id=appointment_id).exists():
            raise serializers.ValidationError("Appointment Doesn't Exist")
        return appointment_id

    def validate_medicine(self, value):
        medicine_id = value.get("id")
        if not Medicince.objects.filter(id=medicine_id).exists():
            raise serializers.ValidationError("Medicine Doesn't Exist")
        return medicine_id

    def validate(self, data):
        medicine_id = data.get("medicine")
        quantity = data.get("quantity")
        medicine = Medicince.objects.get(id=medicine_id)

        balance = medicine.quantity - quantity
        if balance <= 0:
            raise serializers.ValidationError("Quantity not available")

        return super().validate(data)