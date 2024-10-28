from rest_framework import serializers
from drones.models import Competition


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="drones:competitions-detail")
    drone = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name="drones:drones-detail"
    )
    pilot = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name="drones:pilots-detail"
    )

    class Meta:
        model = Competition
        fields = (
            "url",
            "id",
            "distance_in_feet",
            "distance_achievement_date",
            "inserted_timestamp",
            "drone",
            "pilot",
        )
