from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ClinicInfo(models.Model):
    name = models.CharField(max_length=150)
    reg_id = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dob = models.DateField()
    mobile_no = models.CharField(max_length=15)
    role = models.ForeignKey(Role, default=1, on_delete=models.CASCADE)
    address = models.TextField()
    image = models.ImageField(upload_to="profile/staff/images/", blank=True)
    is_active = models.BooleanField(default=True)
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    specialization = models.ManyToManyField(Specialization)
    consultation_fee = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.staff} {self.consultation_fee}"


class BloodGroup(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Patient(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dob = models.DateField()
    mobile_no = models.CharField(max_length=15)
    address = models.TextField()
    image = models.ImageField(upload_to="profile/patient/images/", blank=True)
    is_active = models.BooleanField(default=True)
    is_enable = models.BooleanField(default=True)

    bloodGroup = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
