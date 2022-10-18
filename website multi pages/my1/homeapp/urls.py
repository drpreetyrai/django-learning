from django.contrib import admin
from homeapp import views
from django.urls import path
admin.site.site_header = "UnOrg Admin"
admin.site.site_title = "UnOrg Admin Portal"
admin.site.index_title = "Welcome to UnOrg's Online Thela Portal"

urlpatterns = [
    
    path("", views.index,name='homeapp'),
    path("about", views.about,name='about'),
    path("rules", views.rules,name='rules'),
    path("services", views.services,name='services'),
    path("contact", views.contact,name='contact'),
    path("help", views.help,name='help'),
]
