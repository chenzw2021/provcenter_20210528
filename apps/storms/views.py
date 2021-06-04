import json
from rest_framework import viewsets
from django.core import serializers
from django.http import JsonResponse
from .models import StormProjects


class StormProjectView(viewsets.ModelViewSet):
    def get(self, request):
        """
        通过django的view实现课程列表页
        """
        courses = StormProjects.objects.all()[:10]
        json_data = serializers.serialize('json', courses)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)
