from rest_framework import serializers
from drones.models import Pilot
from .CompetitionSerializer import CompetitionSerializer

class PilotSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="drones:pilots-detail")
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Pilot.GENDER_CHOICES)
    gender_description = serializers.CharField(source="get_gender_display", read_only=True)

    class Meta:
        model = Pilot
        fields = (
            "url",
            "id",
            "name",
            "gender",
            "gender_description",
            "races_count",
            "inserted_timestamp",
            "competitions",
        )
