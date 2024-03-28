from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
import json
from django_redis import get_redis_connection

from apps.consumer.models import Consumer


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
