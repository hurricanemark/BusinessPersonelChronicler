from rest_framework import serializers
from careerJournal.models import Users, Employment

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('UserId', 'UserName', 'UserProfile', 'UserEmail')
        
class EmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employment
        fields=('EmployeeId', 'EmployeeName', 'EmployeeTitle', 'DateOfJoining', 'EmployeeStatus', 'PhotoFileName')