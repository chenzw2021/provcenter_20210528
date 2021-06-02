from rest_framework import serializers
from .models import StormProjects


class StormProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = StormProjects
        fields = '__all__'


class InterfacesByStormProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = StormProjects
        fields = ('interfaces', )

