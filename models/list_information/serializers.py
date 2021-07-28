from .models import ListInformation, CompleteInformationView
from rest_framework import serializers


class ListInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListInformation
        fields = (
            'id',
            'date',
            'person',
            'vaccine',
            'applied_doses',
            'place'
        )

class CompleteInformationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompleteInformationView
        fields = (
            'id',
            'user_id',
            'days',
            'first_dose_date',
            'second_dose_date',
            'first_name',
            'last_name',
            'age',
            'vaccine_name',
            'number_doses',
            'applied_doses',
            'name_place'
        )