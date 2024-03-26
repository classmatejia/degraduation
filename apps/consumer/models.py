from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Consumer(AbstractUser):
    mobile = models.CharField(max_length=11, unique=False, verbose_name='手机号')
    email = models.EmailField(unique=True, verbose_name='邮箱', blank=False, null=False)

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
