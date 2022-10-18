from rest_framework import serializers
from api.models import Student
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=180)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=150)
