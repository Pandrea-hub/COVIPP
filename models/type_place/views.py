from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import TypePlace
from .serializers import TypePlaceSerializer

@permission_classes([AllowAny])
class TypePlaceList(generics.ListCreateAPIView):
    queryset = TypePlace.objects.all()
    serializer_class = TypePlaceSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

@permission_classes([AllowAny])
class TypePlaceDetail(generics.RetrieveUpdateDestroyAPIView):  # TRAER MAS A DETALLE Y HACER PUT AND DELETE
    queryset = TypePlace.objects.all()
    serializer_class = TypePlaceSerializer
