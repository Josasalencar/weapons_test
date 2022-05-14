from uuid import uuid4

from django.db import models

# Create your models here.

class Calibre(models.Model):
    id_calibre = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    desc_calibre =models.CharField(max_length=45)

class Objeto_tipo(models.Model):
    id_objeto_tipo = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tipo_objeto = models.CharField(max_length=64)

class Objeto(models.Model):
    id_objeto = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    objeto_tipo = models.ForeignKey(Objeto_tipo, on_delete=models.CASCADE)

class Arma(models.Model):
    id_arma = models.UUIDField(primary_key=True, default = uuid4,editable=False)
    calibre = models.ForeignKey(Calibre, on_delete=models.CASCADE, null= True)
    objeto = models.ForeignKey(Objeto, on_delete= models.CASCADE, null= True)
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    quantidade_de_tiros = models.IntegerField(default=0)
    valor_estimado = models.FloatField(default=0)
    imagem = models.CharField(max_length=128)

class Municao(models.Model):
    id_municao = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    calibre = models.ForeignKey(Calibre, on_delete=models.CASCADE, null= True)
    objeto = models.ForeignKey(Objeto, on_delete=models.CASCADE, null= True)
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    valor_estimado = models.FloatField(default=0)

