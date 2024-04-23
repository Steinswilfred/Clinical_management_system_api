from django.shortcuts import render
from .models import LabTest,LabTestReport
from .serializers import LabTestReportAddSerializer, LabTestSerializer,LabTestReportSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import permission_classes,api_view
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
# Create your views here.

@csrf_exempt
def test_list(request):
    if request.method == 'GET':
        tes_list = LabTest.objects.all()
        serialized_test_list = LabTestSerializer(tes_list,many=True)
        #FOR JASON CAN ACCEPT DICTIONARY AND DATA TYPE WE USE SAFE=FALSE
        return JsonResponse(serialized_test_list.data,safe=False,status=200)
    elif request.method == 'POST':
        request_date = JSONParser().parse(request)
        test_add_serializer = LabTestSerializer(data=request_date)
        if test_add_serializer.is_valid():
            test_add_serializer.save()
            return JsonResponse(test_add_serializer.data,status=201)

        return JsonResponse(test_add_serializer.errors,status=400)

@csrf_exempt
#@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))
def test_details(request,passed_id):
    test_details = LabTest.objects.get(id=passed_id)
    if request.method == 'GET':
        serialized_test_details = LabTestSerializer(test_details)
        #FOR JASON CAN ACCEPT DICTIONARY AND DATA TYPE WE USE SAFE=FALSE
        return JsonResponse(serialized_test_details.data,safe=False,status=200)

    elif request.method == 'PUT':
        request_date = JSONParser().parse(request)
        test_add_serializer = LabTestSerializer(test_details,data=request_date)
        if test_add_serializer.is_valid():
            test_add_serializer.save()
            return JsonResponse(test_add_serializer.data,status=200)

        return JsonResponse(test_add_serializer.errors,status=400)

    elif request.method == 'DELETE':
        test_details.delete()
        response = "Deleted successfully"
        return HttpResponse(response,status=204)


@csrf_exempt
def testreport_list(request):
    if request.method == 'GET':
        patient_id = request.GET.get("patient")
        print(patient_id)
        if patient_id:
            testreport_list = LabTestReport.objects.filter(
                patient_id=patient_id
            )
        else:
            testreport_list = LabTestReport.objects.all()
        serialized_testreport_list = LabTestReportSerializer(testreport_list,many=True)
        #FOR JASON CAN ACCEPT DICTIONARY AND DATA TYPE WE USE SAFE=FALSE
        return JsonResponse(serialized_testreport_list.data,safe=False,status=200)
    elif request.method == 'POST':
        request_date = JSONParser().parse(request)
        testreport_add_serializer = LabTestReportAddSerializer(data=request_date)
        if testreport_add_serializer.is_valid():
            testreport = testreport_add_serializer.save()
            testreport_serializer = LabTestReportSerializer(testreport)
            return JsonResponse(testreport_serializer.data,status=201)

        return JsonResponse(testreport_add_serializer.errors,status=400)

@csrf_exempt
#@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))
def testreport_details(request,passed_id):
    testreport_details = LabTestReport.objects.get(id=passed_id)
    if request.method == 'GET':
        serialized_testreport_details = LabTestReportSerializer(testreport_details)
        #FOR JASON CAN ACCEPT DICTIONARY AND DATA TYPE WE USE SAFE=FALSE
        return JsonResponse(serialized_testreport_details.data,safe=False,status=200)

    elif request.method == 'PATCH':
        request_date = JSONParser().parse(request)
        testreport_add_serializer = LabTestReportAddSerializer(testreport_details,data=request_date, partial=True)
        if testreport_add_serializer.is_valid():
            testreport = testreport_add_serializer.save()
            testreport_serializer = LabTestReportSerializer(testreport)
            return JsonResponse(testreport_serializer.data,status=200)

        return JsonResponse(testreport_add_serializer.errors,status=400)

    elif request.method == 'DELETE':
        testreport_details.delete()
        response = "Deleted successfully"
        return HttpResponse(response,status=204)