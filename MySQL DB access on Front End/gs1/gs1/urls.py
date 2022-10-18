from django.contrib import admin
from django.urls import path
from api import views
from api.views import student_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/',views.student_detail),
]
