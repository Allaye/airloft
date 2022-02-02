from dataclasses import fields
from rest_framework import serializers
from fleet.models import Aircraft, Airport, Flight


class AirPortSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Airport
        fields = '__all__'
        # extra_kwargs = {'title': {'required': False},'description': {'required': False},'technology': {'required': False},'members': {'required': False}}



class AircraftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aircraft
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = '__all__'
        