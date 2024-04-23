from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class SignupSerializer(serializers.ModelSerializer):
    # Override the user creation function so that
    # We can have the password hashed(encrypted) for token
    def create(self, validated_data):
        # Taking the password from the data user entered and hash it
        # and save it again back to the validated_data
        validated_data["password"] = (make_password(validated_data.get("password")))

        # Create a User and return it
        return super(SignupSerializer, self).create(validated_data)

    class Meta:
        # providing the meta data to the ModelSerializer class
        model = User
        fields = ['username', 'password']

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        # providing the meta data to the ModelSerializer class
        model = User
        fields = ['username', 'password']
        # Getting the username and password through the api