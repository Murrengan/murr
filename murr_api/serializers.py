from rest_framework import serializers
from Murren.models import Murren


class MurrenSerializer(serializers.ModelSerializer):
    class Meta:

        model = Murren
        fields = ('pk', 'username', 'profile_picture')
