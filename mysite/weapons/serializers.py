from rest_framework import serializers
from .models import Arma, Municao
from .models import Objeto_tipo,Objeto

class ArmaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arma
        fields =['id_arma',
                'calibre',
                'marca',
                'modelo',
                'quantidade_de_tiros',
                'valor_estimado',
                'imagem']


class MunicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municao
        fields = ['id_municao',
                'calibre',
                'marca',
                'modelo',
                'valor_estimado']
