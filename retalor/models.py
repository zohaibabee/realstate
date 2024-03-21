from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=100)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d') 
    discription=models.TextField(blank=True)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    is_mvp=models.BooleanField(default=False)
    hire_date=models.DateField(default=datetime.now,blank=True)
    
    
    
    def __str__(self):
        return self.name