from rest_framework import serializers


class ProvRedisSerializer(serializers.ModelSerializer):
    # passid = serializers.CharField(label='车辆通行id', max_length=40, primary_key=True, help_text='车辆通行id')
    # id = serializers.CharField(label='交易流水id', max_length=500, help_text='交易流水id')
    serprovinceid = serializers.CharField(label='通行方id', max_length=500, help_text='通行方id')
    issuerid = serializers.CharField(label='发行方id', max_length=500, help_text='发行方id')
    # mediatype = serializers.CharField(label='介质类型', max_length=500, help_text='介质类型')
    # exitfeetype = serializers.CharField(label='计费类型', max_length=500, help_text='计费类型')
    # datasource = serializers.CharField(label='交易流水类型', max_length=500, help_text='交易流水类型')
    # extime = serializers.CharField(label='出口交易时间', max_length=500, help_text='出口交易时间')
    # payfee = serializers.CharField(label='应收金额', max_length=500, help_text='应收金额')
    # fee = serializers.CharField(label='实收金额', max_length=500, help_text='实收金额')
    # discountfee = serializers.CharField(label='优惠金额', max_length=500, help_text='优惠金额')
    # sumtollfee = serializers.CharField(label='实收金额总和', max_length=500, help_text='实收金额总和')
    # uploadstatus = serializers.CharField(label='上传状态', max_length=500, help_text='上传状态')
    # expassstatus = serializers.CharField(label='交易流水状态', max_length=500, help_text='交易流水状态')
    # gantrypassdata = serializers.CharField(label='门架交易记录信息', max_length=500, help_text='门架交易记录信息')
    # obuprovfeesumafter = serializers.CharField(label='obu省内交易后金额', max_length=500, help_text='obu省内交易后金额')
