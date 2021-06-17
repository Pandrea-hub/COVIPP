from .models import ContagionType
from rest_framework import serializers


class ContagionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContagionType
        fields = (
            'id',
            'name'
        )
