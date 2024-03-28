import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection

from apps.merchant.models import Merchant


# Create your views here.
class RegisterView(View):

    def get(self, request):
        return render(request, 'mcregister.html')

    def post(self, request):
        register_data = json.loads(request.body.decode('utf-8'))
        uuid = register_data.get('captchaUUID')
        merchant_name = register_data.get('consumerName')
        email = register_data.get('email')
        password = register_data.get('password')
        phone = register_data.get('phone')
        # 那到redis中验证码的值
        redis_conn = get_redis_connection('code')
        captcha_value = redis_conn.get(f'img_{uuid}')
        print(uuid, merchant_name, email, phone, password, captcha_value)
        if captcha_value is not None and captcha_value.decode('utf-8') == register_data.get('captcha'):
            # 创建一个新的对象，并保存到数据库中
            Merchant.objects.create(merchantmen=merchant_name, email=email, password=password,
                                    mobile=phone)
            return JsonResponse({'register': 'OK', 'captcha': 1})
        else:
            return JsonResponse({'register': "error", 'captcha': 0})


class MerchantEmailCounter(View):
    """验证用户名是否重复"""

    def post(self, request):
        email = json.loads(request.body.decode('utf-8')).get('email')
        count = Merchant.objects.filter(email=email).count()
        return JsonResponse({'code': 0, 'errmsg': 'OK', 'count': count})


class MeLoginView(View):

    def get(self, request):
        return render(request, 'mclogin.html')

    def post(self, request):
        json_dict = json.loads(request.body.decode('utf-8'))
        username = json_dict.get('username')
        password = json_dict.get('password')
        try:
            me = Merchant.objects.get(merchantmen=username, password=password)
        except Merchant.DoesNotExist:
            return JsonResponse({'code': 400, 'errmsg': '用户名或者密码错误'})
        response = JsonResponse({'code': 200, 'errmsg': 'ok'})
        response.set_cookie('merchant', username.encode("utf-8"), max_age=3600 * 24 * 15)
        request.session['merchant'] = hash(password)
        response.set_cookie('mesessionid', hash(password), max_age=3600 * 24 * 15)
        return response


class MeIndexView(View):

    def get(self, request):
        return render(request, 'mcindex.html')
