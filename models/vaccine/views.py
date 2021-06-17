from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Vaccine
from .serializers import VaccineSerializer


@permission_classes([AllowAny])
class VaccineList(generics.ListCreateAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


@permission_classes([AllowAny])
class VaccineDetail(generics.RetrieveUpdateDestroyAPIView):  # TRAER MAS A DETALLE Y HACER PUT AND DELETE
    queryset = Vaccine.objects.all()  # Trae todos los objetos de place
    serializer_class = VaccineSerializer
