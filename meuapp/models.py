from django.db import models

# Create your models here.

class meuApp(models.Model):
    id_ip = models.IntegerField()
    continentCode = models.CharField(verbose_name = "Código do continente", max_length = 10)
    continentName = models.CharField(verbose_name = "Nome do continente", max_length = 250)
    countryCode = models.CharField(verbose_name = "Código do país", max_length = 10)
    countryName = models.CharField(verbose_name = "Nome do país", max_length = 250)
    countryNameNative = models.CharField(verbose_name = "Nome do país de origem", max_length = 250)
    reionCode = models.CharField(verbose_name = "Código da região", max_length = 10)
    regionName = models.CharField(verbose_name = "Nome da região do país", max_length = 100)
    city = models.CharField(verbose_name = "Nome da cidade", max_length = 250)
    postalCode = models.CharField(verbose_name = "Código postal", max_length = 100)
    latitude = models.CharField(verbose_name = "Latitute", max_length = 100)
    longitude = models.CharField(verbose_name = "Longitute", max_length = 100)
    phoneCode = models.CharField(verbose_name = "Código do número", max_length = 100)
