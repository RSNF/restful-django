from django.urls import include, path
from drones.views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"drone-categories", DroneCategoryViewSet, basename="dronecategory")
router.register(r"drones", DroneViewSet, basename="drones")
router.register(r"pilots", PilotViewSet, basename="pilots")
router.register(r"competitions", CompetitionViewSet, basename="competitions")

urlpatterns = [path("", include(router.urls))]
