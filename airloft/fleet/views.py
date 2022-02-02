from django.db.models import F
from django.db.models.functions import Coalesce, Now
from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from fleet.serializers import (AircraftSerializer, AirPortSerializer, FlightSerializer)
from fleet.models import Airport, Aircraft, Flight
# from employee.permissions import IsOwner, IsProjectMember, IsCurrentUser, IsProjectActive
# from utils.analytics import get_total_project_activity_time, get_individual_project_activity_time
