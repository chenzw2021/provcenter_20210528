import json
from django.views.generic.base import View
from django.core import serializers
from django.http import JsonResponse
from .models import StormProjects


class StormProjectView(View):
    def get(self, request):
        """
        通过django的view实现课程列表页
        """
        courses = StormProjects.objects.all()[:10]
        json_data = serializers.serialize('json', courses)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)