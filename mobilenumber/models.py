from tkinter import CASCADE
from django.db import models
from django.core.validators import RegexValidator
import datetime


# Create your models here.
class phonemodel(models.Model):
   
    phone_number = models.CharField(max_length=17, blank=True) # validators should be a list
    comment= models.CharField(max_length=500)
    status= models.CharField(max_length=10, default="")
    date_reported=models.DateField(default=datetime.datetime.now())
    
    
    def _str_(self):
        return self.phone_number

class reviewmodel(models.Model):
    reviewnumber= models.ForeignKey(phonemodel, on_delete= models.CASCADE)
    review= models.CharField(max_length=500)
    review_status= models.CharField(max_length=20, default="")
    date_posted=models.DateTimeField(default=datetime.datetime.now())
    
    
    # def _str_(self):
    #     return self.reviewnumber