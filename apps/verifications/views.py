from django.http import HttpResponse
from django.views import View
from django_redis import get_redis_connection

from libs.captcha.captcha import captcha


# Create your views here.
class CaptchaView(View):
    """返回图片验证码"""
    def get(self, request, uuid):
        # 生成图片验证码
        text, image = captcha.generate_captcha()

        # 保存图片验证码
        redis_conn = get_redis_connection('code')
        redis_conn.setex(f'img_{uuid}', 300, text)
        # 响应图片验证码
        return HttpResponse(image, content_type='image/jpeg')
