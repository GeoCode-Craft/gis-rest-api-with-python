# Create your views here.
from rest_framework import viewsets
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from rest_framework_gis.filters import DistanceToPointFilter

from . models import  NairobiSubCounties,NairobiHealthFacilities
from . serializers import  NairobiSubCountiesSerializer, NairobiHealthFacilitiesSerializer

class NairobiSubCountiesViewSet(viewsets.ModelViewSet):
	serializer_class = NairobiSubCountiesSerializer
	queryset = NairobiSubCounties.objects.all()


class NairobiHealthFacilitiesViewSet(viewsets.ModelViewSet):
	serializer_class = NairobiHealthFacilitiesSerializer
	queryset = NairobiHealthFacilities.objects.all()
