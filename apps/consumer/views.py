from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
import json
from apps.consumer.models import Consumer


# Create your views here.
class RegisterView(View):
    """注册页面"""

    def get(self, request):
        """get请求返回页面"""
        return render(request, "register.html")

    def post(self, request):
        """post请求传递数据创建用户"""
        pass


class ConsumerEmailCounter(View):
    """验证用户名是否重复"""

    def post(self, request):
        email = json.loads(request.body.decode('utf-8')).get('email')
        count = Consumer.objects.filter(email=email).count()
        return JsonResponse({'code': 0, 'errmsg': 'OK', 'count': count})


class LoginView(View):

    def get(self, request):
        return HttpResponse('login')
