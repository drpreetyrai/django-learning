from django.db import models


#makemigrations-create changes and store in a file
#migrate-apply the pending changes made by make makemigrations
# Create your models here.

class Help(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
     return self.email


 


