from django.shortcuts import render
from .models import ListInformation
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ListInformationSerializer, CompleteInformationListSerializer
from .models import CompleteInformationView


class ListInformationList(generics.ListCreateAPIView):  # GET AND POST
    queryset = ListInformation.objects.all()
    serializer_class = ListInformationSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj



class ListInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListInformation.objects.all()
    serializer_class = ListInformationSerializer


@permission_classes([AllowAny])
class CompleteInformationListView(generics.ListAPIView):  # GET
    serializer_class = CompleteInformationListSerializer

    def get_queryset(self):
        return CompleteInformationView.objects.all().distinct()