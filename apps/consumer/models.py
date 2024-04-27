from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
<<<<<<< HEAD
from django.utils import timezone
=======
>>>>>>> origin/main

from apps.merchant.models import Merchant
from apps.shop.models import Goods


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


class Orders(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Consumer, on_delete=models.CASCADE, related_name='orders', null=False)
    is_comment = models.BooleanField(default=False, verbose_name='Is Comment')
    shop = models.ForeignKey('shop.Shop', on_delete=models.CASCADE, related_name='orders', null=False)
    goods = models.ManyToManyField(Goods, related_name='orders', verbose_name='goods')

    class Meta:
        db_table = 'orders'
        verbose_name = '订单'
        verbose_name_plural = verbose_name

<<<<<<< HEAD
    def __str__(self):
        return ''
=======
>>>>>>> origin/main

class Comment(models.Model):
    Level = (('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5))
    content = models.TextField(max_length=300, verbose_name='评论')
    mark = models.CharField(max_length=10, choices=Level, verbose_name='评分')
    date = models.DateField(auto_now_add=True)
<<<<<<< HEAD
    fk_user = models.ForeignKey(Consumer, related_name='comments', on_delete=models.CASCADE, null=False,verbose_name='user')
    fk_shop = models.ForeignKey('shop.Shop', related_name='comments', on_delete=models.CASCADE, null=False, default='',verbose_name='shop')
=======
    fk_user = models.ForeignKey(Consumer, related_name='comments', on_delete=models.CASCADE, null=False)
    fk_shop = models.ForeignKey('shop.Shop', related_name='comments', on_delete=models.CASCADE, null=False,default='')
>>>>>>> origin/main

    class Meta:
        db_table = 'comments'
        verbose_name = '评论'
        verbose_name_plural = verbose_name


class Browser(models.Model):
    user = models.ForeignKey(Consumer, on_delete=models.CASCADE, related_name='browser')
<<<<<<< HEAD
    shop = models.ForeignKey('shop.Shop', on_delete=models.CASCADE, related_name='browsers')
    date = models.DateTimeField(auto_now_add=True)  # 使用DateTimeField来存储日期和时间信息
=======
    date = models.DateField(auto_now_add=True)
>>>>>>> origin/main

    class Meta:
        db_table = 'browser'
        verbose_name = '浏览记录'
        verbose_name_plural = verbose_name


@receiver(post_save, sender=Browser)
def limit_browser_records(sender, instance, **kwargs):
    max_records = 100
    user = instance.user
<<<<<<< HEAD
    shop = instance.shop
    # 检查是否存在相同用户和相同商店的浏览记录
    existing_record = Browser.objects.filter(user=user, shop=shop)
    if len(existing_record) > 1:
        # 如果存在，更新该记录的日期时间为当前时间
        existing_record.update(date=timezone.localtime())
        instance.delete()
        # 如果不存在，创建新的浏览记录
    current_count = Browser.objects.filter(user=user).count()
    if current_count >= max_records:
        # 如果记录数量已达到最大限制，则删除最旧的记录
        oldest_record = Browser.objects.filter(user=user).order_by('date').first()
        oldest_record.delete()
        instance.save()
        # 创建新的浏览记录
=======
    current_count = Browser.objects.filter(user=user).count()
    if current_count > max_records:
        oldest_record = Browser.objects.filter(user=user).order_by('date').first()
        oldest_record.delete()
>>>>>>> origin/main
