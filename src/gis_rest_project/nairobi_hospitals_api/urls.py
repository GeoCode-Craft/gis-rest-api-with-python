# nairobi_hospitals_api/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'nairobisubounties', views.NairobiCountyViewSet)
router.register(r'nairobihealthfacilities', views.NairobiHealthFacilitiesViewSet)
router.register(r'nairobicounty', views.NairobiCountyViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]