from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView          # so that normal views can return API data
from rest_framework.response import Response
from rest_framework import status                 # sends back status
from .models import employees
from .serializers import employeesSerializer
# Create your views here.

class employeeList(APIView):

    def  get(self, request):
        employee1 = employees.objects.all()
        serializer = employeesSerializer(employee1, many= True)  # 2nd param states that there are more than one employees, so don;t return one json object
        return Response(serializer.data)

    def post(self):
        pass


