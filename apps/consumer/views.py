from django.http import HttpResponse, JsonResponse
from django.views import View
import json

from django_redis import get_redis_connection

from apps.consumer.models import Consumer
from libs.captcha.captcha import captcha


# Create your views here.
class RegisterView(View):

    def get(self, request):
        return HttpResponse('register')


class ConsumerCounter(View):
    """验证用户名是否重复"""

    def post(self, request):
        consumer_name = json.loads(request.body.decode('utf-8')).get('consumer_name')
        count = Consumer.objects.filter(username=consumer_name).count()
        return JsonResponse({'code': 0, 'errmsg': 'OK', 'count': count})


class LoginView(View):

    def get(self, request):
        return HttpResponse('login')


