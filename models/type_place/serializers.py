from .models import TypePlace
from rest_framework import serializers


class TypePlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePlace
        fields = (
            'id',
            'name'
        )
