from rest_framework import serializers
from fleet.models import Aircraft, Airport, Flight


class AirPortSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Airport
        fields = '__all__'
        # extra_kwargs = {'title': {'required': False},'description': {'required': False},'technology': {'required': False},'members': {'required': False}}



