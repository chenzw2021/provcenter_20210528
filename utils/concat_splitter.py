redis_gantrypassdata_val = ["id", "passid", "gantrytype", "type", "transtime",
                            "payfee", "fee", "discountfee", "specialtype"]
redis_main_val = ["id", "serprovinceid", "issuerid", "mediatype", "exitfeetype", "datasource", "extime",
                  "payfee", "fee", "discountfee", "sumtollfee", "uploadstatus", "expassstatus",
                  "gantrypassdata", 'obuprovfeesumafter']


def concat_split(concat_res):
    try:
        concat_res = concat_res.decode().split(",")
    except AttributeError:
        data = {"msg": "无数据"}
    else:
        gantry_li = [dict(zip(redis_gantrypassdata_val, i.split(";"))) for i in concat_res[-2].split("#")
                     if not concat_res[-2] == "null"]  # 对gantrypassdata拆分
        concat_res[-2] = "null" if not gantry_li else sorted(gantry_li, key=lambda x: (x["transtime"]))
        # 对gantrypassdata按transtime升序排列
        data = dict(zip(redis_main_val, concat_res))
    return data
