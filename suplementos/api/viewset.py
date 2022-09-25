from rest_framework import viewsets
from suplementos.api import serializers
from suplementos import models

class SuplementoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SuplementoSerializer
    queryset = models.Suplemento.objects.all()