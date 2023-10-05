from rest_framework import serializers
from models import Morador

class PerfilMoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = '__all__'