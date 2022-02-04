from dataclasses import fields
import django_filters
from fleet.models import Aircraft, Airport, Flight


# class FlightFilter(django_filters.FilterSet):
#     """
#     Filter class for Flight
#     """

#     departure_airport = django_filters.ModelChoiceFilter(
#         name="departure_airport", query_set=Flight.objects.all(), lookup_expr="exact"
#     )

#     class Meta:
#         model = Flight
#         fields = [
#             "id",
#             "aircraft",
#             "arrival_time",
#             "departure_time",
#             "arrival_airport",
#             "departure_airport",
#         ]


class FlightFilter(django_filters.FilterSet):
    description = django_filters.CharFilter()
    departure_airport= django_filters.CharFilter(field_name="departure_airport__name", lookup_expr="iexact")
    arrival_airport_name = django_filters.CharFilter(lookup_expr="icontains")
    aircraft = django_filters.CharFilter(field_name="aircraft__name", lookup_expr="iexact")

    # release_year = django_filters.NumberFilter(field_name='release_date', lookup_expr='year')
    # release_year__gt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__gt')
    # release_year__lt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__lt')

    # manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Flight
        fields = "__all__"
