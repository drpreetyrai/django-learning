from django.contrib import admin
from django.urls import path
from api import views#added manually
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('stuinfo/', views.student_list),#added manually
    path('stuinfo/<int:pk>', views.student_detail),#added manually
]