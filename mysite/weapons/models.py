from uuid import uuid4

from django.db import models

# Create your models here.

class Arma(models.Model):
    id_arma = models.UUIDField(primary_key=True, default = uuid4,editable=False)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    quantidade_de_tiros = models.IntegerField(default=0)
    valor_estimado = models.FloatField(default=0)
    imagem = models.CharField(max_length=255)

class Municao(models.Model):
    id_municao = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    valor_estimado = models.FloatField(default=0)

