from django.db import models


class ProvredisDetail(models.Model):
    passid = models.CharField(verbose_name='车辆通行id', max_length=40, primary_key=True, help_text='车辆通行id')
    id = models.CharField(verbose_name='交易流水id', max_length=500, help_text='交易流水id')
    serprovinceid = models.CharField(verbose_name='通行方id', max_length=500, help_text='通行方id')
    issuerid = models.CharField(verbose_name='发行方id', max_length=500, help_text='发行方id')
    mediatype = models.CharField(verbose_name='介质类型', max_length=500, help_text='介质类型')
    exitfeetype = models.CharField(verbose_name='计费类型', max_length=500, help_text='计费类型')
    datasource = models.CharField(verbose_name='交易流水类型', max_length=500, help_text='交易流水类型')
    extime = models.CharField(verbose_name='出口交易时间', max_length=500, help_text='出口交易时间')
    payfee = models.CharField(verbose_name='应收金额', max_length=500, help_text='应收金额')
    fee = models.CharField(verbose_name='实收金额', max_length=500, help_text='实收金额')
    discountfee = models.CharField(verbose_name='优惠金额', max_length=500, help_text='优惠金额')
    sumtollfee = models.CharField(verbose_name='实收金额总和', max_length=500, help_text='实收金额总和')
    uploadstatus = models.CharField(verbose_name='上传状态', max_length=500, help_text='上传状态')
    expassstatus = models.CharField(verbose_name='交易流水状态', max_length=500, help_text='交易流水状态')
    gantrypassdata = models.CharField(verbose_name='门架交易记录信息', max_length=500, help_text='门架交易记录信息')
    obuprovfeesumafter = models.CharField(verbose_name='obu省内交易后金额', max_length=500, help_text='obu省内交易后金额')

    class Meta:
        db_table = 'tb_redis_main'
        verbose_name = '行程组合主表'
        verbose_name_plural = verbose_name


class Provredis(models.Model):
    id = models.CharField(verbose_name='门架校验记录id', max_length=500,primary_key=True, help_text='门架校验记录id')
    passid = models.CharField(verbose_name='车辆通行id', max_length=40, help_text='车辆通行id')
    gantrytype = models.CharField(verbose_name='门架类型', max_length=500, help_text='门架类型')
    type = models.CharField(verbose_name='门架介质类型', max_length=500, help_text='门架介质类型')
    transtime = models.CharField(verbose_name='交易时间', max_length=500, help_text='交易时间')
    payfee = models.CharField(verbose_name='应收金额', max_length=500, help_text='应收金额')
    fee = models.CharField(verbose_name='实收金额', max_length=500, help_text='实收金额')
    discountfee = models.CharField(verbose_name='优惠金额', max_length=500, help_text='优惠金额')
    specialtype = models.CharField(verbose_name='特情类型', max_length=500, help_text='特情类型')

    class Meta:
        db_table = 'tb_redis_detail'
        verbose_name = '行程组合子表'
        verbose_name_plural = verbose_name





