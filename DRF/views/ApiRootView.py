from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

from drones.views import DroneViewSet


class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "drones": {
                    "drone-categories": reverse(
                        "drones:dronecategory-list", request=request
                    ),
                    "drones": reverse("drones:drones-list", request=request),
                    "pilots": reverse("drones:pilots-list", request=request),
                    "competitions": reverse(
                        "drones:competitions-list", request=request
                    ),
                },
                "core": {
                    "livros": reverse("core:livros-list", request=request),
                    "autores": reverse("core:autores-list", request=request),
                    "categorias": reverse("core:categorias-list", request=request),
                },
                "swagger": {
                    "schema": reverse("schema", request=request),
                    "swagger": reverse("swagger-ui", request=request),
                },
                "auth": {"api-token-auth": reverse("api-token-auth", request=request)},
            }
        )
