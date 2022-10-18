from django.shortcuts import render
from api.serializers import StudentSerializer
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from api.models import Student

# MOdel object single student data
def student_detail(request,pk):
    stu=Student.objects.get(id=pk)#creating model object
    #print(stu)
    serializer=StudentSerializer(stu)#converting model object to python data type
    #print(serializer)
    #print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)#converting python data type JSON Data Type
    # #print(json_data)
    return HttpResponse(json_data,content_type='application/json')#JSON data send to client
    return JsonResponse(serializer.data)

#Query set all student data
def student_list(request):
    stu=Student.objects.all()
    print(stu)
    serializer=StudentSerializer(stu,many=True)
    # print(serializer)
    # print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data,content_type='application/json')
    # return JsonResponse(serializer.data, safe=False)