from django.shortcuts import render
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from api.serializers import StudentSerializer
# Create your views here.
def student_detail(request):
    stu=Student.objects.get(id=1)#created model object i.e. complex data type
    serializer=StudentSerializer(stu)#converted complex data to python object
    json_data=JSONRenderer().render(serializer.data)#converted to JSON
    return HttpResponse(json_data,content_type='application/json')#JSON is sent to client
    