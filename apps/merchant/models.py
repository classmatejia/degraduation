from django.db import models


# Create your models here.
class Merchant(models.Model):
    merchantmen = models.CharField(max_length=30, verbose_name='姓名')
    email = models.EmailField(max_length=125, verbose_name='邮箱', unique=True)
    password = models.CharField(max_length=128, verbose_name='密码')
    mobile = models.CharField(max_length=11, unique=False, verbose_name='手机号', default=None)

    class Meta:
        db_table = 'mc_users'
        verbose_name = '商家'
        verbose_name_plural = verbose_name
