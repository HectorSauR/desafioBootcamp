from rest_framework import serializers
# from rest_framework.exceptions import ValidationError

from .models import Mantenimiento

class MantenimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mantenimiento
        exclude = ["kilometraje"]