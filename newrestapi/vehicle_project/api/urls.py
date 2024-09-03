from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, upload_csv

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)

urlpatterns = [
    path('upload/', upload_csv),
    path('', include(router.urls)),
]
