from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Appointment,Appointment_Bill
from .serializers import AppointmentSerializer,AppointmentBillSerializer,AppointmentAddSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from cms_admin.models import Patient


@csrf_exempt
def appointment_list(request):
    if request.method == "GET":
        doctor_id = request.GET.get("doctor")
        if doctor_id:
            appointment_list = Appointment.objects.filter(
                doctor__staff_id=doctor_id, is_done=False
            )
        else:
            appointment_list = Appointment.objects.all()
        #serialize the query set
        serialized_appointment_list = AppointmentSerializer(appointment_list, many=True)#many equals to true bcs we are processing a list
        return JsonResponse(serialized_appointment_list.data,safe=False,status=200)

@csrf_exempt
def appointment(request, id):
    if request.method == "GET":
        appointment_list = get_object_or_404(Appointment, pk=id)
        #serialize the query set
        serialized_appointment_list = AppointmentSerializer(appointment_list)#many equals to true bcs we are processing a list
        return JsonResponse(serialized_appointment_list.data,safe=False,status=200)
        #for json to accept dictionaries and other data type

@csrf_exempt
def appointment_add(request):
    if request.method == "POST":
        request_data = JSONParser().parse(request)
        #using the serializer, serialize the parsed json

        appointment_add_serializer = AppointmentAddSerializer(data=request_data)
        #if the serializer returned a valid serialized data
        if appointment_add_serializer.is_valid():
            appointment = appointment_add_serializer.save()
            serializer = AppointmentSerializer(appointment)
            #send back the response code and a copy of data added as json
            return JsonResponse(serializer.data , status=201)
        return JsonResponse(appointment_add_serializer.errors, status=400)

@csrf_exempt
def appointment_edit(request, id):
    if request.method == "PATCH":
        appointment = get_object_or_404(Appointment, pk=id)
        request_data = JSONParser().parse(request)
        #using the serializer, serialize the parsed json
        appointment_add_serializer = AppointmentAddSerializer(appointment, data=request_data, partial=True)
        #if the serializer returned a valid serialized data
        if appointment_add_serializer.is_valid():
            appointment = appointment_add_serializer.save()
            serializer = AppointmentSerializer(appointment)
            #send back the response code and a copy of data added as json
            return JsonResponse(serializer.data , status=201)
        return JsonResponse(appointment_add_serializer.errors, status=400)

@csrf_exempt
def appointment_bill(request):
    if request.method == "GET":
        appointment_bill = Appointment_Bill.objects.all()
        #serialize the query set
        serialized_appointment_list = AppointmentBillSerializer(appointment_bill, many=True)#many equals to true bcs we are processing a list
        return JsonResponse(serialized_appointment_list.data,safe=False,status=200)
        #for json to accept dictionaries and other data type
