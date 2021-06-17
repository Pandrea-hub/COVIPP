from .models import Place
from rest_framework import serializers


# Crea format del JSON

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            'id',
            'title',
            'draggable',
            'fragment',
            'longitude',
            'latitude',
            'type_place'

        )
