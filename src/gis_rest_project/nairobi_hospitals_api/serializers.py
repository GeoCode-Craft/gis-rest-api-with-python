from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import NairobiCounty, NairobiSubCounties,NairobiHealthFacilities



class NairobiCountySerializer(GeoFeatureModelSerializer):

	class Meta:
		model = NairobiCounty
		fields = '__all__'
		geo_field = 'geom'


class NairobiSubCountiesSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = NairobiSubCounties
		fields = '__all__'
		geo_field = 'geom'


class NairobiHealthFacilitiesSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = NairobiHealthFacilities
		fields = '__all__'
		geo_field = 'geom'