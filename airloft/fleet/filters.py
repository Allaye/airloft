from dataclasses import fields
import django_filters
from fleet.models import Flight


class FlightFilter(django_filters.FilterSet):
    description = django_filters.CharFilter()
    departure_airport = django_filters.CharFilter(field_name="departure_airport__name", lookup_expr="iexact")
    arrival_airport = django_filters.CharFilter(field_name="arrival_airport_name", lookup_expr="iexact")
    aircraft = django_filters.CharFilter(field_name="aircraft__name", lookup_expr="iexact")

    departure_time__gt = django_filters.NumberFilter(field_name='departure_time', lookup_expr='year__gt')
    departure_time__lt = django_filters.NumberFilter(field_name='departure_time', lookup_expr='year__lt')
    arrival_time__gt = django_filters.NumberFilter(field_name='arrival_time', lookup_expr='year__gt')
    arrival_time__lt = django_filters.NumberFilter(field_name='arrival_time', lookup_expr='year__lt')

    # manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Flight
        fields = "__all__"
