from rest_framework import serializers
from .models import Murr


class MurrSerializer(serializers.ModelSerializer):

    class Meta:

        model = Murr
        fields = ('title', 'description', 'timestamp', 'author', 'cover',  'slug')
