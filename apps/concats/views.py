from django.http import HttpResponse, JsonResponse
from django.views import View
from django_redis import get_redis_connection
from .serializers import ConcatSerializer
from utils.concat_splitter import concat_split

conn = get_redis_connection()


class ConcatView(View):

    # def get(self, request):
    #     concat_val = conn.get('{014401204022700008915720210506233530}OBU')
    #     data = concat_split(concat_val)
    #     redis_obj = ProvRedisSerializer(instance=data)
    #         # redis_obj.is_valid(raise_exception=True)
    #     # return JsonResponse(redis_obj.data, safe=False, json_dumps_params={'ensure_ascii': False})
    #     return JsonResponse(redis_obj.data)

    def post(self, request):
        concat_val = conn.get(request.POST['passid'])
        data = concat_split(concat_val)
        redis_obj = ConcatSerializer(instance=data)
        return JsonResponse(redis_obj.data)

