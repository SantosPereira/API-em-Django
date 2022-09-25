from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from suplementos.models import Suplemento

class SuplementoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suplemento
        fields = '__all__'