from django.db import models
from datetime import datetime
from retalor.models import Realtor
# Create your models here.

class Listing(models.Model):
    realtor=models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    adress=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=20)
    discription=models.TextField(max_length=700,blank=True,default=None)
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    batrooms=models.DecimalField(max_digits=2,decimal_places=1)
    grage=models.IntegerField(default=0)
    sqft=models.IntegerField()
    lot_size=models.DecimalField(max_digits=5,decimal_places=1)
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published=models.BooleanField(default=True)
    list_date=models.DateField(default=datetime.now,blank=True)
    
    
    
    
   
