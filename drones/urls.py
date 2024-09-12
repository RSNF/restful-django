from django.urls import include, path
from drones.views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"drone-categories", DroneCategoryViewSet)
router.register(r"drones", DroneViewSet)
router.register(r"pilots", PilotViewSet)
router.register(r"competitions", CompetitionViewSet)

urlpatterns = [
    path("", include(router.urls))
]
