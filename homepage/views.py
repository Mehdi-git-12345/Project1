from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Employeeserialezers


def insertEmployee(request):
    employee = Employee.objects.create(
        first_name = "Mehdi",
        last_name='Jn',
        email="mehdijn@gmail.com",
        salary=7500.44
    )
    return render(request, "success.html",{"employee":employee})

def hello(request):
    return HttpResponse("hi")

@api_view(['GET'])
def getEmployee(request):
    employees = Employee.objects.all()
    serializer = Employeeserialezers(employees,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addEmployee(request):
    serializer = Employeeserialezers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    else :
        return Response(serializer.errors,status=400) 

  





# Create your views here.
