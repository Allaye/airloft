from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView)
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from fleet.filters import FlightFilter
from fleet.serializers import (AircraftSerializer, AirPortSerializer, FlightSerializer)
from fleet.models import Airport, Aircraft, Flight
from django_filters.rest_framework import DjangoFilterBackend

class CreateAircraftApiview(CreateAPIView):
    """
    create a new aircraft endpoint, this endpoint is protected by the IsAdminuser permission
    only admin users can access this endpoint
    """
    serializer_class = AircraftSerializer
    permission_classes = (IsAdminUser) # protect the endpoint
    def perform_create(self, serializer):
        return serializer.save()

class RetriveAircraftApiView(ListAPIView):
    """
    Retrive all project activities by current user
    permission_classes = "IsAuthenticated"
    any user logged in can access this endpoint
    """
    serializer_class = AircraftSerializer
    permission_classes = (IsAuthenticated,) # protect the endpoint
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name','serial_number', 'model', 'manufacturer']
    def get_queryset(self):
        return Aircraft.objects.filter()

class CreateAirportApiview(CreateAPIView):
    """
    create a new airport endpoint, this endpoint is protected by isAdminUser permission
    only admin users can create new airport
    """
    serializer_class = AirPortSerializer
    permission_classes = (IsAdminUser) # protect the endpoint
    def perform_create(self, serializer):
        return serializer.save()

class RetriveAirportApiView(ListAPIView):
    """
    retrieve all or single airport details by id
    permission_classes = "IsAuthenticated"
    any user logged in can access this endpoint
    """
    serializer_class = AirPortSerializer
    permission_classes = (IsAuthenticated,) # protect the endpoint
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name','location', 'code']
    def get_queryset(self):
        return Airport.objects.filter()


class CreateFlightApiview(CreateAPIView):
    """
    create a new flight endpoint, this endpoint is protected by isAdminUser permission
    only admin users can create new flight
    """
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated, IsAdminUser) # protect the endpoint
    def perform_create(self, serializer):
        return serializer.save()

class RetriveFlightApiView(ListAPIView):
    """
    Retrive all project activities by current user
    permission_classes = "IsAuthenticated" :user is logged in
    """
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated,) # protect the endpoint
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = FlightFilter
    # filterset_fields = ['id', 'aircraft','departure_airport', 'arrival_airport', 'departure_time', 'arrival_time']
    #search_fields = ['aircraft','departure_time', 'arrival_time']
    def get_queryset(self):
        return Flight.objects.filter()

class UpdateFlightApiview(UpdateAPIView):
    """
    Update a flight object, and return the updated object.
    permission_classes = "IsAdminUser"
    only admin can update a flight details
    """
    serializer_class = FlightSerializer
    permission_classes = (IsAdminUser) # protect the endpoint
    queryset = Flight.objects.all()
    fields = ['description', 'aircraft', 'departure_time', 'arrival_time']
    def perform_update(self, serializer):
        return serializer.save()

class DestroyFlightApiview(DestroyAPIView):
    """
    Delete a flight object.
    Permission_classes = "IsAdminUser"
    only admin can delete a flight
    """
    serializer_class = FlightSerializer
    permission_classes = (IsAdminUser)  # protect the endpoint
    queryset = Flight.objects.all()

    def perform_destroy(self, instance):
        return instance.delete()