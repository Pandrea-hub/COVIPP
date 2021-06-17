from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Place
from .serializers import PlaceSerializer


class PlaceByPlaceType(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def get_queryset(self):
        type_place_id = self.kwargs['type_place_id']
        if 'place_id' in self.kwargs:
            place_id = self.kwargs['place_id']
            return Place.objects.filter(type_place=type_place_id, pk=place_id).distinct()
        else:
            return Place.objects.filter(type_place=type_place_id).distinct()



class PlaceList(generics.ListCreateAPIView):  # GET AND POST
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):  # TRAER MAS A DETALLE Y HACER PUT AND DELETE
    queryset = Place.objects.all()  # Trae todos los objetos de place
    serializer_class = PlaceSerializer
