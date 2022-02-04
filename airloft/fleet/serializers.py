from dataclasses import fields
from rest_framework import serializers
from fleet.models import Aircraft, Airport, Flight


class AirPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = "__all__"
        # extra_kwargs = {'title': {'required': False},'description': {'required': False},'technology': {'required': False},'members': {'required': False}}


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = "__all__"


class FlightSerializer(serializers.ModelSerializer):
    # aircraft = serializers.RelatedField(read_only=True)
    # departure_airport = serializers.StringRelatedField(many=False)
    # arrival_airport = serializers.StringRelatedField(many=False)
    # aircraft = serializers.StringRelatedField(many=False)
    aircraft = serializers.SlugRelatedField(
        slug_field="name", queryset=Aircraft.objects.all()
    )

    # departure_airport = serializers.SlugRelatedField(
    #     slug_field="name", queryset=Airport.objects.all()
    # )
    # arrival_airport = serializers.SlugRelatedField(
    #     slug_field="name", queryset=Airport.objects.all()
    # )


    class Meta:
        model = Flight
        fields = "__all__"
