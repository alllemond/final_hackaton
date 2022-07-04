
from .models import Movie
from django_filters.rest_framework import FilterSet 


class MovieGenreCountryFilter(FilterSet):

    class Meta:
        model = Movie
        fields = ('genre',)
