from django.shortcuts import render
from rest_framework import  viewsets
from .models import Arma,Municao
from .serializers import ArmaSerializer,MunicaoSerializer

class ArmaViewSet(viewsets.ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer

class MunicaoViewSet(viewsets.ModelViewSet):
    queryset = Municao.objects.all()
    serializer_class = MunicaoSerializer
