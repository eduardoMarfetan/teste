from rest_framework import viewsets
from meuapp.api import serializer
from meuapp import models

class meuappViewSets(viewsets.ModelViewSet):
    serializer_class = serializer.meuappSerializer
    queryset = models.meuApp.objects.all()