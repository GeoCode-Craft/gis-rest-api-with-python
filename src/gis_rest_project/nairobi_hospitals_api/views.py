# Create your views here.
from rest_framework import viewsets

from django_filters import rest_framework  as filters
from . hospitals_filters import NairobiHealthFacilitiesFilter
from . models import  NairobiSubCounties,NairobiHealthFacilities
from . serializers import  NairobiSubCountiesSerializer, NairobiHealthFacilitiesSerializer

class NairobiSubCountiesViewSet(viewsets.ModelViewSet):
	serializer_class = NairobiSubCountiesSerializer
	queryset = NairobiSubCounties.objects.all()


class NairobiHealthFacilitiesViewSet(viewsets.ModelViewSet):
    serializer_class = NairobiHealthFacilitiesSerializer
    queryset = NairobiHealthFacilities.objects.all()
    filterset_class = NairobiHealthFacilitiesFilter
    filter_backends = [filters.DjangoFilterBackend]
   
