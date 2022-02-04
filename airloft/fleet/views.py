from re import search
from django.db.models import F
from django.db.models.functions import Coalesce, Now
from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView)
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from fleet.filters import FlightFilter
from fleet.serializers import (AircraftSerializer, AirPortSerializer, FlightSerializer)
from fleet.models import Airport, Aircraft, Flight
from django_filters.rest_framework import DjangoFilterBackend
# from employee.permissions import IsOwner, IsProjectMember, IsCurrentUser, IsProjectActive
# from utils.analytics import get_total_project_activity_time, get_individual_project_activity_time

class CreateAircraftApiview(CreateAPIView):
    """

    """
    serializer_class = AircraftSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser) # protect the endpoint
    def perform_create(self, serializer):
        return serializer.save()

class RetriveAircraftApiView(ListAPIView):
    """
    Retrive all project activities by current user
    permission_classes = "IsAuthenticated" :user is logged in
    """
    serializer_class = AircraftSerializer
    # permission_classes = (IsAuthenticated,) # protect the endpoint
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name','serial_number', 'model', 'manufacturer']
    def get_queryset(self):
        return Aircraft.objects.filter()

class CreateAirportApiview(CreateAPIView):
    """

    """
    serializer_class = AirPortSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser) # protect the endpoint
    def perform_create(self, serializer):
        return serializer.save()
class RetriveAirportApiView(ListAPIView):
    """
    
    """
    serializer_class = AirPortSerializer
    # permission_classes = (IsAuthenticated,) # protect the endpoint
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name','location', 'code']
    def get_queryset(self):
        return Airport.objects.filter()


class CreateFlightApiview(CreateAPIView):
    """

    """
    serializer_class = FlightSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser) # protect the endpoint
    def perform_create(self, serializer):
        return serializer.save()

class RetriveFlightApiView(ListAPIView):
    """
    Retrive all project activities by current user
    permission_classes = "IsAuthenticated" :user is logged in
    """
    serializer_class = FlightSerializer
    # permission_classes = (IsAuthenticated,) # protect the endpoint
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = FlightFilter
    # filterset_fields = ['id', 'aircraft','departure_airport', 'arrival_airport', 'departure_time', 'arrival_time']
    #search_fields = ['aircraft','departure_time', 'arrival_time']
    def get_queryset(self):
        return Flight.objects.filter()

