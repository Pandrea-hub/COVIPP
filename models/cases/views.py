from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from .models import Cases, CasesSymptomView, CasesContagionView
from .serializers import CasesSerializer, CasesByContagionSerializer, CasesBySymptomSerializer, \
    CasesByPersonAndCaseSerializer


class CasesBySymptom(generics.ListAPIView):
    serializer_class = CasesBySymptomSerializer

    def get_queryset(self):
        person_id = self.kwargs['person_id']
        return CasesSymptomView.objects.filter(id=person_id).distinct()


class CasesByContagion(generics.ListAPIView):
    serializer_class = CasesByContagionSerializer

    def get_queryset(self):
        person_id = self.kwargs['person_id']
        return CasesContagionView.objects.filter(id=person_id).distinct()


class CasesByPerson(generics.ListCreateAPIView):
    queryset = Cases.objects.all()
    serializer_class = CasesSerializer

    def get_queryset(self):
        person_id = self.kwargs['person_id']
        if 'cases_id' in self.kwargs:
            cases_id = self.kwargs['cases_id']
            return Cases.objects.filter(person=person_id, pk=cases_id).distinct()
        else:
            return Cases.objects.filter(person=person_id).distinct()




class CasesByPersonAndCase(generics.ListCreateAPIView):
    queryset = Cases.objects.all()
    serializer_class = CasesSerializer

    def get_queryset(self):
        person_id = self.kwargs['person_id']
        if 'cases_id' in self.kwargs:
            cases_id = self.kwargs['cases_id']
            return Cases.objects.filter(person=person_id, pk=cases_id).distinct()
        else:
            return Cases.objects.filter(person=person_id).distinct()





class CasesByContagionType(generics.ListCreateAPIView):  # Crea un JOIN entre cases y contagion type
    queryset = Cases.objects.all()
    serializer_class = CasesSerializer

    def get_queryset(self):
        contagion_type_id = self.kwargs['contagion_type_id']
        if 'cases_id' in self.kwargs:
            cases_id = self.kwargs['cases_id']
            return Cases.objects.filter(contagion_type=contagion_type_id, pk=cases_id).distinct()
        else:
            return Cases.objects.filter(contagion_type=contagion_type_id).distinct()






class CasesList(generics.ListCreateAPIView):  # GET AND POST
    queryset = Cases.objects.all()
    serializer_class = CasesSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


class CasesDetail(generics.RetrieveUpdateDestroyAPIView):  # TRAER MAS A DETALLE Y HACER PUT AND DELETE
    queryset = Cases.objects.all()
    serializer_class = CasesSerializer
