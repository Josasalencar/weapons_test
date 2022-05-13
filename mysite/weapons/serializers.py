from rest_framework import serializers
from .models import Arma, Municao

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = ['id', 'marca', 'modelo', 'quantidade_de_tiros','valor_estimado','imagem']


class MunicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municao
        fields = ['id', 'marca', 'modelo', 'valor_estimado']
