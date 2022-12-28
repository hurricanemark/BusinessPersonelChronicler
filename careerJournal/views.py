from django.shortcuts import render
# csrf allows other domains to access our methods
from django.views.decorators.csrf import csrf_exempt
# JSONParser to parse incoming data models
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from careerJournal.models import Users, Employment
from careerJournal.serializers import UsersSerializer, EmploymentSerializer

# storage module
from django.core.files.storage import default_storage


# Create your views here.
# CRUD operations for the users table
@csrf_exempt
def usersApi(request, id=0):
    if request.method=='GET':
        users = Users.objects.all()
        user_serializer = UsersSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    elif request.method=='POST':
        user_data = JSONParser().parse(request)
        users_serializer = UsersSerializer( data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe= False)
    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user = Users.objects.get(UserId=user_data['UserId'])
        users_serializer = UsersSerializer(user, data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        user = Users.objects.get(UserId=id)
        user.delete()
        return JsonResponse("Delete Successfully", safe=False)
        


# CRUD operations for the employment table
@csrf_exempt
def employmentApi(request, id=0):
    if request.method=='GET':
        employees = Employment.objects.all()
        employee_serializer = EmploymentSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    elif request.method=='POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmploymentSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe= False)
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee = Employment.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer = EmploymentSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method=='DELETE':
        employee = Employment.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Delete Successfully", safe=False)
    
    
@csrf_exempt
def saveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
    