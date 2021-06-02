from rest_framework import serializers
from .models import Interfaces


class InterfacesSerializer(serializers.ModelSerializer):
    storm_project = serializers.StringRelatedField()

    class Meta:
        model = Interfaces
        fields = '__all__'

