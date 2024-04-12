import json
import re

from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection

from apps.shop.models import *
from .models import *


# Create your views here.
class RegisterView(View):
    """注册页面"""

    def get(self, request):
        """get请求返回页面"""
        return render(request, "register.html")

    def post(self, request):
        register_data = json.loads(request.body.decode('utf-8'))
        # 获取json中的数据
        uuid = register_data.get('captchaUUID')
        consumer_name = register_data.get('consumerName')
        email = register_data.get('email')
        password = register_data.get('password')
        phone = register_data.get('phone')
        # 那到redis中验证码的值
        redis_conn = get_redis_connection('code')
        captcha_value = redis_conn.get(f'img_{uuid}')

        if captcha_value is not None and captcha_value.decode('utf-8') == register_data.get('captcha'):
            # 创建一个新的Consumer对象，并保存到数据库中
            user = Consumer.objects.create_user(username=consumer_name, email=email, password=password, mobile=phone)
            if register_data.get('loginDirectly'):
                login(request, user)
            return JsonResponse({'register': 'OK', 'captcha': 1})
        else:
            return JsonResponse({'register': "error", 'captcha': 0})


class ConsumerEmailCounter(View):
    """验证用户名是否重复"""

    def post(self, request):
        email = json.loads(request.body.decode('utf-8')).get('email')
        count = Consumer.objects.filter(email=email).count()
        return JsonResponse({'code': 0, 'errmsg': 'OK', 'count': count})


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        json_dict = json.loads(request.body.decode('utf-8'))
        username = json_dict.get('username')
        password = json_dict.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({'code': 400, 'errmsg': '用户名或者密码错误'})
        else:
            login(request, user)
            request.session.set_expiry(None)
            response = JsonResponse({'code': 200, 'errmsg': 'ok'})
            # 注册时用户名写入到cookie，有效期15天
            response.set_cookie('username', user.username.encode("utf-8"), max_age=3600 * 24 * 15)

            return response


class LogoutView(View):
    """退出登录"""

    def delete(self, request):
        """实现退出登录逻辑"""
        # 清理session
        logout(request)
        # 退出登录，重定向到登录页
        response = JsonResponse({'code': 200,
                                 'errmsg': 'ok'})
        # 退出登录时清除cookie中的username
        response.delete_cookie('username')

        return response


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')


class CategoryView(View):

    def get(self, request, num):
        b_type = ShopsType.objects.get(id=num)
        shops = b_type.type.all()
        context = {
            "shops": [
                {"id": f"{i.id}", 'name': f"{i.shop_name}", "address": f"{i.adders}", "mark": f"{i.mark}"} for i in
                shops
            ]
        }
        return render(request, 'category.html', context=context)


class ShopView(View):

    def get(self, request, num):
        shop = Shop.objects.get(id=num)
        goods_list = shop.goods.all()
        is_commented = False
        if request.user.is_authenticated:
            comment = shop.comments.filter(fk_user=request.user)
            if comment:  #
                is_commented = True
            else:
                is_commented = False
        comments = shop.comments.all()
        context = {
            'business': {'name': shop.shop_name, 'address': shop.adders, 'phone': shop.phone,"mark":shop.mark},
            'products': [{"id": i.id, 'name': i.goods_name, 'price': i.price} for i in goods_list],
            'condition': is_commented,
            'comments': [{'user': i.fk_user, 'text': i.content} for i in comments]
        }
        return render(request, 'shop.html', context=context)

    def post(self, request, num):
        if request.user.is_authenticated:
            json_dict = json.loads(request.body.decode('utf-8'))
            id_list = []
            for i in json_dict:
                id_list.append(int(i['id']))
            goods_instances = Goods.objects.filter(pk__in=id_list)
            shop = Shop.objects.get(id=num)

            Orders.objects.create(
                user=request.user,
                is_comment=False,
                shop=shop,
            ).goods.add(*goods_instances)

            return JsonResponse({"code": 200})
        else:
            # 用户未登录
            return JsonResponse({"code": 400})


class CommentView(View):

    def post(self, request):
        if request.user.is_authenticated:
            json_dict = json.loads(request.body.decode('utf-8'))
            comment = json_dict.get('comment')
            num = json_dict.get('path')
            mark = int(json_dict.get('mark'))
            print(mark)
            match = re.search(r'\d+$', num)
            if match:
                # 返回匹配到的数字
                id = match.group()
            else:
                # 如果没有匹配到数字，返回 None 或者您想要的默认值
                return JsonResponse({"code": 400})
            shop = Shop.objects.get(id=id)
            shop.mark = round((int(shop.mark) + mark) / 2, 1)
            shop.save()
            Comment.objects.create(
                content=comment,
                fk_user=request.user,
                fk_shop=shop,
                mark=mark
            )
            return JsonResponse({"code": 200})
        else:
            return JsonResponse({"code": 400})


class CartView(View):
    def post(self, request, ):
        json_dict = json.loads(request.body.decode('utf-8'))
        id = int(json_dict['id'])
        goods = Goods.objects.get(id=id)
        return JsonResponse({"name": goods.goods_name})
