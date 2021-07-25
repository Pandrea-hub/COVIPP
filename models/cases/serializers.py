from .models import Cases, CasesSymptomView, CasesContagionView
from rest_framework import serializers

from .views import CasesByPersonAndCase


class CasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cases
        fields = (
            'id',
            'date',
            'contagion_type',
            'person'
        )


class CasesBySymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasesSymptomView
        fields = (
            'id',
            'case_id',
            'first_day',
            'contagion_day',
            'not_contagion_day',
            'not_covid',
            'first_name',
            'last_name'
        )


class CasesByContagionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasesContagionView
        fields = (
            'id',
            'case_id',
            'firsts_day',
            'infectious_day',
            'symptom_day',
            'free_covid',
            'not_infectious_day',
            'first_name',
            'last_name'
        )

class CasesByPersonAndCase(serializers.ModelSerializer):
    class Meta:
        model = CasesByPersonAndCase
        fields = (
            'id',
            'person_id',
            'contagion_type'
        )
