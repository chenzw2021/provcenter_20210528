from rest_framework import serializers
from .models import ConcatMain, ConcatDetail


class ConcatSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcatMain
        fields = '__all__'

