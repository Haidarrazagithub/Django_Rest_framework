from django.shortcuts import render
from .models import Device, Clinic
from .serializers import DiviceSerializer, ClinicSerializer
from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class DeviceLists(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DiviceSerializer
    filterset_fields = ['device_id']


class DeviceList(generics.RetrieveUpdateDestroyAPIView):
    page_size =4
    page_size_query_param = 'page_size'
    max_page_size = 10
    queryset = Device.objects.all()
    serializer_class = DiviceSerializer
    filterset_fields = ['device_id']


class ClinicLists(generics.ListCreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    filterset_fields = ['name']


class ClinicList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    filterset_fields = ['name']
