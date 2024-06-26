from cms_admin.models import Staff
from cms_admin.serializers import StaffSerializer
from .serializers import LoginSerializer, SignupSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password

class SignupAPIView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            json_response = {'status': status.HTTP_201_CREATED}
            return Response(json_response, status=status.HTTP_201_CREATED)
        else:
            json_response = {'status': status.HTTP_400_BAD_REQUEST, 'data': serializer.errors}
            return Response(json_response, status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
def DeleteUser(request,passed_id):
    fetch = User.objects.get(id=passed_id)
    if request.method == "DELETE":
        fetch.delete()
        response = "Deleted successfully"
        return HttpResponse(response,status=204)
    
# Create your views here.
# class LoginAPIView(APIView):
#     # The post function t handle post request
#     def post(self, request):
#         # Create the serializer object from our SignupSerializer
#         serializer = LoginSerializer(data=request.data)
#         # If the data or the serializer is valid, then create the user and send 201 status
#         if serializer.is_valid():
#             username = serializer.validated_data["username"]
#             password = serializer.validated_data["password"]
#             # Trying to authenticate the user
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 # The user was successfully authenticated, we can get his Token
#                 token = get_object_or_404(Token, user=user)
#                 staff = get_object_or_404(Staff, user=user)
#                 serializer = StaffSerializer(staff)
#                 response = {
#                     "username": username,
#                     "staff": serializer.data,
#                     "token": token.key
#                 }
#                 return Response(response, status=status.HTTP_200_OK)
#             else:
#                 response = {
#                     "status": status.HTTP_401_UNAUTHORIZED,
#                     "message": "Sorry Invalid username or password",
#                 }
#                 return Response(response, status=status.HTTP_401_UNAUTHORIZED)

#         response = {
#             "status": status.HTTP_400_BAD_REQUEST,
#             "message": "Sorry it was a bad request",
#             "data": serializer.errors
#         }
#         return Response(response, status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    # The post function to handle post request
    def post(self, request):
        # Create the serializer object from our SignupSerializer
        serializer = LoginSerializer(data=request.data)
        # If the data or the serializer is valid, then create the user and send 201 status
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            # Trying to authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Check if the user already has a token
                token, created = Token.objects.get_or_create(user=user)
                if not created:
                    token.delete()
                    token = Token.objects.create(user=user)

                staff = get_object_or_404(Staff, user=user)
                serializer = StaffSerializer(staff)
                response = {
                    "username": username,
                    "staff": serializer.data,
                    "token": token.key
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "Sorry Invalid username or password",
                }
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)

        response = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "Sorry it was a bad request",
            "data": serializer.errors
        }
        return Response(response, status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    def post(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        if not check_password(old_password, user.password):
            return Response({'message': 'Old password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

        if len(new_password) < 8:
            return Response({'message': 'New password must be at least 8 characters long.'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)

