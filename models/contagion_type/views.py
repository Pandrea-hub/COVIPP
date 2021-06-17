from django.shortcuts import render
from .models import ContagionType
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from .serializers import ContagionTypeSerializer


# Create your views here.

@permission_classes([AllowAny])
class ContagionTypeList(generics.ListCreateAPIView):  # GET AND POST
    queryset = ContagionType.objects.all()
    serializer_class = ContagionTypeSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


@permission_classes([AllowAny])
class ContagionTypeDetail(generics.RetrieveUpdateDestroyAPIView):  # TRAER MAS A DETALLE Y HACER PUT AND DELETE
    queryset = ContagionType.objects.all()
    serializer_class = ContagionTypeSerializer
