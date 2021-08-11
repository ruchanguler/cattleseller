from django.db import models

# Create your models here.
class Cattle(models.Model):
    buyer = models.CharField(max_length=50,null=True,verbose_name="İsim",unique=True)
    salesorder = models.CharField(max_length=50,null=True,verbose_name="Satış Sırası",unique=True)
    cattleid = models.CharField(max_length=50,null=True,verbose_name="Hayvan Numarası",unique=True)
    slaughterorder = models.CharField(max_length=50,null=True,verbose_name="Kesim Sırası",unique=True)
    phonenumber = models.IntegerField(null=True,verbose_name="Telefon Numarası",unique=True)
 