from django.db import models


class StormProjects(models.Model):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField('Storm任务名称', max_length=200, unique=True, help_text='Storm任务名称')
    leader = models.CharField('负责人', max_length=50, help_text='项目负责人')
    tester = models.CharField('测试人员', max_length=50, help_text='项目测试人员')
    programmer = models.CharField('开发人员', max_length=50, help_text='开发人员')
    publish_app = models.CharField('发布应用', max_length=100, help_text='发布应用')
    desc = models.CharField('简要描述', max_length=200, null=True, blank=True, default='', help_text='简要描述')

    class Meta:
        db_table = 'tb_storm_projects'
        verbose_name = 'Storm任务信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
