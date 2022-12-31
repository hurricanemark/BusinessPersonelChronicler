from django.db import models

# Create your models here.
class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=500)
    UserProfile = models.CharField(max_length=500)
    UserEmail = models.EmailField(max_length=50)
    
class Employment(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    EmployeeTitle = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    EmployeeStatus = models.CharField(max_length=100)
    PhotoFileName = models.CharField(max_length=500, null=True)
