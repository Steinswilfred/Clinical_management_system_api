from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser

from pharmacist.models import Medicince, MedicinePrescriptionBill, Medistate
from pharmacist.serializers import MedicineAddSerializer, MedicinePrescriptionAddBillSerializer, MedicinePrescriptionBillSerializer, MedicineSerializer, MedicineStateSerializer

from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def medicince_list(request):
    if  request.method == "GET":
        medicince_list= Medicince.objects.all()
    # fetching  all the deta and save it
    # serialize the query
        serialized_medicince_list= MedicineSerializer(medicince_list,many=True)
       # return the serialized object as a JSON response
        return JsonResponse(serialized_medicince_list.data, safe=False, status=200)
    elif request.method == 'POST':
        request_data = JSONParser().parse(request)   # DEFAULT PARAMETER
        medicince_add_serializer = MedicineAddSerializer(data=request_data)
        #SERIALIZE THE PARSE JSON
        if medicince_add_serializer.is_valid():
            # if serializer returned a valid serialized data
            medicine = medicince_add_serializer.save()
            medicine_serializer = MedicineSerializer(medicine)
            return JsonResponse(medicine_serializer.data, status=201)
            # send back response code  and the copy
        return JsonResponse(medicince_add_serializer.errors, status=400)


@csrf_exempt
def medicince_details(request,passed_id):
    # get the details of the post with it passed id
    medicince_details = get_object_or_404(Medicince, pk=passed_id)
    if request.method == "GET":
     # serialize the query
        serialized_medicince_details=MedicineSerializer(medicince_details)
       # return the serialized object as a JSON response
        return JsonResponse(serialized_medicince_details.data, safe=False, status=200)
    elif request.method== 'PATCH':
        request_data= JSONParser().parse(request)   # DEFAULT PARAMETER
        medicince_edit_serializer = MedicineAddSerializer(medicince_details,data=request_data, partial=True)
        #SERIALIZE THE PARSE JSON
        if medicince_edit_serializer.is_valid():
            # if serializer returned a valid serialized data
            medicine = medicince_edit_serializer.save()
            medicine_serializer = MedicineSerializer(medicine)
            return JsonResponse(medicine_serializer.data, status=200)
            # send back response code  and the copy
        return JsonResponse(medicince_edit_serializer.error, status=400)
    

@csrf_exempt
def medistate_list(request):
    if  request.method == "GET":
        medistate_list= Medistate.objects.all()
    # fetching  all the deta and save it
    # serialize the query
        serialized_medistate_list= MedicineStateSerializer(medistate_list,many=True)
       # return the serialized object as a JSON response
        return JsonResponse(serialized_medistate_list.data, safe=False, status=200)
    elif request.method == 'POST':
        request_data = JSONParser().parse(request)   # DEFAULT PARAMETER
        medistate_add_serializer = MedicineStateSerializer(data=request_data)
        #SERIALIZE THE PARSE JSON
        if medistate_add_serializer.is_valid():
            # if serializer returned a valid serialized data
            medistate_add_serializer.save()
            return JsonResponse(medistate_add_serializer.data, status=201)
            # send back response code  and the copy
        return JsonResponse(medistate_add_serializer.errors, status=400)


@csrf_exempt
def medistate_details(request,passed_id):
    # get the details of the post with it passed id
    medistate_details = get_object_or_404(Medistate, pk=passed_id)
    if request.method == "GET":
     # serialize the query
        serialized_medistate_details=MedicineSerializer(medistate_details)
       # return the serialized object as a JSON response
        return JsonResponse(serialized_medistate_details.data, safe=False, status=200)
    elif request.method== 'PUT':
        request_data= JSONParser().parse(request)   # DEFAULT PARAMETER
        medistate_edit_serializer = MedicineStateSerializer(medistate_details,data=request_data)
        #SERIALIZE THE PARSE JSON
        if medistate_edit_serializer.is_valid():
            # if serializer returned a valid serialized data
            medistate_edit_serializer.save()
            return JsonResponse(medistate_edit_serializer.data, status=200)
            # send back response code  and the copy
        return JsonResponse(medistate_edit_serializer.error, status=400)
    elif request.method == 'DELETE':
        medistate_details.delete()
        response= "Deleted Successfully"
        return HttpResponse(response,status=204)

@csrf_exempt
def medicine_bill(request):
    if  request.method == "GET":
        medicines_bill= MedicinePrescriptionBill.objects.all()
        serialized_medicines_bill_list= MedicinePrescriptionBillSerializer(medicines_bill,many=True)
        return JsonResponse(serialized_medicines_bill_list.data, safe=False, status=200)
    elif request.method == 'POST':
        medicine_bill = JSONParser().parse(request)   # DEFAULT PARAMETER
        medicines_bill_add_serializer = MedicinePrescriptionAddBillSerializer(data=medicine_bill, many=True)

        if medicines_bill_add_serializer.is_valid():
            medicines_bill_add_serializer.save()
            return JsonResponse(medicines_bill_add_serializer.data, safe=False, status=201)
        return JsonResponse(medicines_bill_add_serializer.errors, safe=False, status=400)
    
def medicine_bill_details(request,passed_id):
        fetch = MedicinePrescriptionBill.objects.get(id=passed_id)
        if request.method == 'GET':
            serialize = MedicinePrescriptionBillSerializer(fetch)
            return JsonResponse(serialize.data,safe=False,status=200)
        elif request.method == 'PUT':
            put = JSONParser().parse(request)
            putseraize = MedicinePrescriptionBillSerializer(fetch,data=put)
            if putseraize.is_valid():
                putseraize.save()
                return JsonResponse(putseraize.data,status=200)
            return JsonResponse(putseraize.errors,status=400)
        elif request.method == 'DELETE':
            response = "Deleted successfully"
            return HttpResponse(response,status=204)