# Create your views here.
from rest_framework import viewsets

from . models import NairobiCounty, NairobiSubCounties,NairobiHealthFacilities
from . serializers import NairobiCountySerializer, NairobiSubCountiesSerializer, NairobiHealthFacilitiesSerializer


class NairobiCountyViewSet(viewsets.ModelViewSet):
	serializer_class = NairobiCountySerializer
	queryset = NairobiCounty.objects.all() 


class NairobiSubCountiesViewSet(viewsets.ModelViewSet):
	serializer_class = NairobiSubCountiesSerializer
	queryset = NairobiSubCounties.objects.all()


class NairobiHealthFacilitiesViewSet(viewsets.ModelViewSet):
	serializer_class = NairobiHealthFacilitiesSerializer
	queryset = NairobiHealthFacilities.objects.all() or NairobiHealthFacilities.objects.filter(poly__within= NairobiSubCounties.pk)