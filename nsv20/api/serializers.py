from dataclasses import fields
from msilib.schema import Class
from rest_framework import serializers
from .models import Device,Clinic

class DiviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Device
        fields='__all__'

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Clinic
        fields='__all__'
