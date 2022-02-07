from django.urls import path
from . import views


urlpatterns = [

    path("create/aircraft", views.CreateAircraftApiview.as_view(), name="add_airraft"),
    path("create/airport", views.CreateAirportApiview.as_view(), name="add_airport"),
    path("create/flight", views.CreateFlightApiview.as_view(), name="add_flight"),
    path("flight/", views.RetriveFlightApiView.as_view(), name="flight_list"),
    path("aircraft/", views.RetriveAircraftApiView.as_view(), name="aircraft_list"),
    path("airport/", views.RetriveAirportApiView.as_view(), name="airport_list"),
    path("flight/<int:pk>", views.RetriveFlightApiView.as_view(), name="flight_update"),
    path("aircraft/<int:pk>", views.DestroyFlightApiview.as_view(), name="aircraft_delete"),
]
