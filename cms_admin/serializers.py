from django.contrib.auth.models import User

from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import (
    BloodGroup,
    ClinicInfo,
    Doctor,
    Patient,
    Role,
    Specialization,
    Staff,
)


class ClinicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicInfo
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class RoleIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Role
        fields = ("id",)

    def validate_id(self, value):
        return value


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username",)

class UserIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = User
        fields = ("id",)

    def validate_id(self, value):
        return value


class StaffSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    user = UserSerializer()

    class Meta:
        model = Staff
        fields = "__all__"

class StaffAddSerializer(serializers.ModelSerializer):
    role = RoleIdSerializer()
    user = UserIdSerializer()

    class Meta:
        model = Staff
        exclude = ("image",)

    def create(self, validated_data):
        role_id = validated_data.pop("role")
        user_id = validated_data.pop("user")

        staff = Staff.objects.create(**validated_data, role_id=role_id, user_id=user_id)
        return staff

    def update(self, instance, validated_data):
        staff = instance
        staff.first_name = validated_data.get("first_name", staff.first_name)
        staff.last_name = validated_data.get("last_name", staff.last_name)
        staff.dob = validated_data.get("dob", staff.dob)
        staff.mobile_no = validated_data.get("mobile_no", staff.mobile_no)
        staff.address = validated_data.get("address", staff.address)
        staff.image = validated_data.get("image", staff.image)
        staff.is_active = validated_data.get("is_active", staff.is_active)
        staff.is_enable = validated_data.get("is_enable", staff.is_enable)

        # Get the role_id and user_id from validated_data
        role_id = validated_data.get("role", {}).get("id")
        user_id = validated_data.get("user", {}).get("id")

        # Ensure that role_id and user_id are provided
        if role_id is not None:
            staff.role_id = role_id
        if user_id is not None:
            staff.user_id = user_id

        staff.save()

        return staff

    def validate_role(self, value):
        role_id = value.get("id")
        if not Role.objects.filter(id=role_id).exists():
            raise serializers.ValidationError("Role Doesn't Exist")
        return role_id

    def validate_user(self, value):
        user_id = value.get("id")
        if user_id != 0:
            if not User.objects.filter(id=user_id).exists():
                raise serializers.ValidationError("User Doesn't Exist")
            elif Staff.objects.filter(user_id=user_id).exists():
                raise serializers.ValidationError("Staff Already Exist")

        return user_id

class StaffIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Staff
        fields = ("id",)

    def validate_id(self, value):
        return value


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"


class SpecializationIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Specialization
        fields = ("id",)

    def validate_id(self, value):
        return value


class DoctorSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    specialization = SpecializationSerializer(many=True)

    class Meta:
        model = Doctor
        fields = "__all__"


class DoctorIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Doctor
        fields = ("id",)

    def validate_id(self, value):
        return value


# class DoctorAddSerializer(serializers.ModelSerializer):
#     staff = StaffAddSerializer()
#     specialization = SpecializationIdSerializer(many=True)

#     class Meta:
#         model = Doctor
#         fields = "__all__"

#     def create(self, validated_data):
#         specialization_ids = validated_data.pop("specialization")
#         staff_data = validated_data.pop("staff")

#         designation_ids = staff_data.pop("designation")
#         role_id = staff_data.pop("role")
#         user_id = staff_data.pop("user")
#         designations = Designation.objects.filter(id__in=designation_ids)
#         staff = Staff.objects.create(**staff_data, role_id=role_id, user_id=user_id)
#         staff.designation.set(designations)
#         staff.save()

#         specializations = Specialization.objects.filter(id__in=specialization_ids)
#         doctor = Doctor.objects.create(**validated_data, staff=staff)
#         doctor.specialization.set(specializations)
#         doctor.save()

#         return doctor

#     def update(self, instance, validated_data):
#         doctor = instance

#         if validated_data.get("staff"):
#             staff_data = validated_data.pop("staff")
#             staff = instance.staff
#             staff.first_name = staff_data.get("first_name", staff.first_name)
#             staff.last_name = staff_data.get("last_name", staff.last_name)
#             staff.dob = staff_data.get("dob", staff.dob)
#             staff.mobile_no = staff_data.get("mobile_no", staff.mobile_no)
#             staff.address = staff_data.get("address", staff.address)
#             staff.image = staff_data.get("image", staff.image)
#             staff.is_active = staff_data.get("is_active", staff.is_active)
#             staff.is_enable = staff_data.get("is_enable", staff.is_enable)

#             if staff_data.get("designation"):
#                 designations = Designation.objects.filter(
#                     id__in=staff_data.get("designation")
#                 )
#                 staff.designation.set(designations)

#             staff.save()
#             doctor.staff = staff

#         if validated_data.get("specialization"):
#             specialization_ids = validated_data.pop("specialization")
#             specializations = Specialization.objects.filter(id__in=specialization_ids)
#             doctor.specialization.set(specializations)

#         doctor.consultation_fee = validated_data.get(
#             "consultation_fee", doctor.consultation_fee
#         )
#         doctor.save()

#         return doctor

#     def validate_specialization(self, values):
#         specialization_ids = []
#         for value in values:
#             designation_id = value.get("id")
#             if not Specialization.objects.filter(id=designation_id).exists():
#                 raise serializers.ValidationError("Specialization Doesn't Exist")
#             specialization_ids.append(designation_id)

#         return specialization_ids

#     def validate_staff(self, value):
#         if Doctor.objects.filter(staff_id=value.get("id")).exists():
#             raise serializers.ValidationError("Doctor Already Exist")

#         return value


class DoctorAddSerializer(serializers.ModelSerializer):
    staff = StaffAddSerializer()
    specialization = SpecializationIdSerializer(many=True)

    class Meta:
        model = Doctor
        fields = "__all__"

    def create(self, validated_data):
        specialization_ids = validated_data.pop("specialization")
        staff_data = validated_data.pop("staff")

        role_id = staff_data.pop("role")
        user_id = staff_data.pop("user")
        
        # Creating Staff instance
        staff = Staff.objects.create(role_id=role_id, user_id=user_id, **staff_data)

        specializations = Specialization.objects.filter(id__in=specialization_ids)

        # Creating Doctor instance
        doctor = Doctor.objects.create(staff=staff, **validated_data)
        doctor.specialization.set(specializations)
        
        return doctor

    def update(self, instance, validated_data):
        doctor = instance

        if validated_data.get("staff"):
            staff_data = validated_data.pop("staff")
            staff = instance.staff
            staff.first_name = staff_data.get("first_name", staff.first_name)
            staff.last_name = staff_data.get("last_name", staff.last_name)
            staff.dob = staff_data.get("dob", staff.dob)
            staff.mobile_no = staff_data.get("mobile_no", staff.mobile_no)
            staff.address = staff_data.get("address", staff.address)
            staff.image = staff_data.get("image", staff.image)
            staff.is_active = staff_data.get("is_active", staff.is_active)
            staff.is_enable = staff_data.get("is_enable", staff.is_enable)
            staff.save()
            doctor.staff = staff

        if validated_data.get("specialization"):
            specialization_ids = validated_data.pop("specialization")
            specializations = Specialization.objects.filter(id__in=specialization_ids)
            doctor.specialization.set(specializations)

        doctor.consultation_fee = validated_data.get(
            "consultation_fee", doctor.consultation_fee
        )
        doctor.save()

        return doctor

    def validate_specialization(self, values):
        specialization_ids = []
        for value in values:
            specialization_id = value.get("id")
            if not Specialization.objects.filter(id=specialization_id).exists():
                raise serializers.ValidationError("Specialization Doesn't Exist")
            specialization_ids.append(specialization_id)

        return specialization_ids

class BloodGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodGroup
        fields = "__all__"


class BloodGroupIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = BloodGroup
        fields = ("id",)

    def validate_id(self, value):
        return value


class PatientSerializer(serializers.ModelSerializer):
    bloodGroup = BloodGroupSerializer()

    class Meta:
        model = Patient
        fields = "__all__"


class PatientIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Patient
        fields = ("id",)

    def validate_id(self, value):
        return value


class PatientAddSerializer(serializers.ModelSerializer):
    bloodGroup = BloodGroupIdSerializer()

    class Meta:
        model = Patient
        fields = "__all__"

    def create(self, validated_data):
        bloodGroup_id = validated_data.pop("bloodGroup")
        patient = Patient.objects.create(**validated_data, bloodGroup_id=bloodGroup_id)
        return patient

    def update(self, instance, validated_data):
        patient = instance
        patient.first_name = validated_data.get("first_name", patient.first_name)
        patient.last_name = validated_data.get("last_name", patient.last_name)
        patient.dob = validated_data.get("dob", patient.dob)
        patient.mobile_no = validated_data.get("mobile_no", patient.mobile_no)
        patient.address = validated_data.get("address", patient.address)
        patient.image = validated_data.get("image", patient.image)
        patient.is_active = validated_data.get("is_active", patient.is_active)
        patient.is_enable = validated_data.get("is_enable", patient.is_enable)
        patient.bloodGroup_id = validated_data.get("bloodGroup", patient.bloodGroup_id)
        patient.save()
        return patient

    def validate_bloodGroup(self, value):
        bloodGroup_id = value.get("id")
        if not BloodGroup.objects.filter(id=bloodGroup_id).exists():
            raise serializers.ValidationError("BloodGroup Doesn't Exist")

        return bloodGroup_id
