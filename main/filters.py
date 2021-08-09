import django_filters
from .models import *

class CattleFilter(django_filters.FilterSet):
    class Meta:
        model = Cattle
        fields =  ("buyer","salesorder","cattleid","slaughterorder")