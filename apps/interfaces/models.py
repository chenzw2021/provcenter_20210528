from django.db import models


class Interfaces(models.Model):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField(verbose_name='接口名称', max_length=200, unique=True, help_text='接口名称')
    storm_project = models.ForeignKey('storms.StormProjects', on_delete=models.CASCADE,
                                      related_name='interfaces', help_text='Storm任务名称')
    tester = models.CharField(verbose_name='测试人员', max_length=50, help_text='测试人员')
    desc = models.CharField(verbose_name='简要描述', max_length=200, null=True, blank=True, help_text='简要描述')

    class Meta:
        db_table = 'tb_interfaces'
        verbose_name = '接口信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
