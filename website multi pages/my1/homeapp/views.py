from datetime import datetime
from homeapp.models import Help
from django.shortcuts import render, HttpResponse
from django.contrib import messages
def index(request): 
     context = {
          "var_name1":"varriable_value1, ",
          "var_name2":"varriable_value2, ",
          "var_name3":"varriable_value3, ",
          "var_name4":"varriable_value4, ",
          "var_name5":"varriable_value5"
          }
     
     return render(request,'index.html',context)
     #return HttpResponse("this is new HomePage")
def help(request):
     if request.method=="POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          desc=request.POST.get('desc')
          help=Help(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
          help.save()
          messages.success(request, 'Your Details are saved.')
     return render(request,'help.html')
def about(request):
     return render(request,'about.html')
    # return HttpResponse("this is new About Page")
def rules(request):
     return render(request,'rules.html')
    ## return HttpResponse("this is new Rules Page")
def services(request):
     messages.success(request,"this is my string")
     return render(request,'services.html')
    # return HttpResponse("this is new Services Page")
def contact(request):
     return render(request,'contact.html')
     #return HttpResponse("this is new Contact Page")

     
     

     
    # return render(request,'help.html')
    # return HttpResponse("this is new Help Page")
# Create your views here.
