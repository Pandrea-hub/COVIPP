from .models import Vaccine
from rest_framework import serializers


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = (
            'id',
            'name',
            'days',
            'number_doses'
        )

