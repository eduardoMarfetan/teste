from rest_framework import serializers
from meuapp import models

class meuappSerializer(serializers.ModelSerializer):
    class meta:
        model = models.meuApp
        fields = '__all__'