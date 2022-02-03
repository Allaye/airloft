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

class CreateProjectApiview(CreateAPIView):
    """Create a new project object, and return the created object.
    permission_classes = "IsAuthenticated" :user is logged in , "IsAdminUser" : user is admin
    Post: /api/create/project
    Endpoint: Post: /api/create/project
    Authorization: Bearer <eyJ0eXAiOiJKV1QiLCJhunXe-dxoFCEY5l2VGkeRR8ue-Ggr6YxQS2nJUA63VZ4>
    Request body:{
    "name": "project pholoa",
    "description": "blockchain systems to track spent time",
    "technology": {"technology":"blockchain"},
    "members": [1,4,2]           // this are the members ids added to the project (project members)
    "start_date": "2022-01-01",  // if left blank it defaults to today
    }

    Response:{
    "id": 3,
    "is_completed": false,
    "title": "",
    "description": "blockchain systems to track spent time",
    "technology": {
        "technology": "blockchain"
    },
    "start_date": "2022-01-01",
    "end_date": null,
    "members": [1, 4, 2]
    }
    
    Error Response:{
       "status_code": 403,
         "detail": "You do not have permission to perform this action."
    }


    """
    serializer_class = AircraftSerializer
    permission_classes = (IsAuthenticated, IsAdminUser) # protect the endpoint
    def perform_create(self, serializer):
        return serializer.save()


    
