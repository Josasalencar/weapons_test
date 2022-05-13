from django.db import models

# Create your models here.

class Arma(models.Model):
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    quantidade_de_tiros = models.IntegerField(default=0)
    valor_estimado = models.FloatField(default=0)
    imagem = models.CharField(max_length=128)

class Municao(models.Model):
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    valor_estimado = models.FloatField(default=0)

