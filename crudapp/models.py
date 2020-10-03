from django.db import models

# Create your models here.
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    firstname = models.CharField(max_length=30)  
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=45)  
    contact = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=200)  
    class Meta:  
        db_table = "employee"