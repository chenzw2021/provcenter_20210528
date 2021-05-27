from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render
from django_cluster_redis.cache import ClusterRedis
from django_redis import get_redis_connection

conn = get_redis_connection()


class PyRedis(View):

    # def get(self, request):
    #     data = [{"project": "项目1",
    #              "test": "czw1",
    #              "msg": "111"},
    #             {"project": "项目2",
    #              "test": "czw2",
    #              "msg": "222"},
    #             {"project": "项目3",
    #              "test": "czw3",
    #              "msg": "333"}]
    #     # return render(request, 'index.html', locals())
    #     return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def get(self, request):
        # data = conn.get('{014401204022700008915720210506233530}OBU')
        redis_gantrypassdata_val = ["ID", "PASSID", "GANTRYTYPE", "TYPE", "TRANSTIME",
                                         "PAYFEE", "FEE", "DISCOUNTFEE", "SPECIALTYPE"]
        redis_main_val = ["ID", "SERPROVINCEID", "ISSUERID", "MEDIATYPE", "EXITFEETYPE", "DATASOURCE", "EXTIME",
                               "PAYFEE", "FEE", "DISCOUNTFEE", "SUMTOLLFEE", "UPLOADSTATUS", "EXPASSSTATUS",
                               "GANTRYPASSDATA", 'OBUPROVFEESUMAFTER']
        try:
            redis_msg = conn.get('{014401204022700008915720210506233530}OBU').decode().split(",")
        except AttributeError:
            return '无缓存数据'
        else:
            gantry_li = [dict(zip(redis_gantrypassdata_val, i.split(";"))) for i in redis_msg[-2].split("#")
                         if not redis_msg[-2] == "null"]  # 对gantrypassdata拆分
            redis_msg[-2] = "null" if not gantry_li else sorted(gantry_li, key=lambda x: (x["TRANSTIME"]))
            # 对gantrypassdata按transtime升序排列
            data = dict(zip(redis_main_val, redis_msg))
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
