import json
from email.mime.text import MIMEText
from email.header import Header
from django.http import HttpResponse, JsonResponse
from django.views import View
from django_redis import get_redis_connection
import smtplib
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


# class SendEmailView(View):
#
#     def post(self, request):
#         # 创建 SMTP 对象
#         smtp = smtplib.SMTP()
#         # 连接（connect）指定服务器
#         smtp.connect("smtp.126.com", port=25)
#         # 登录，需要：登录邮箱和授权码
#         smtp.login(user="classmatejia@126.com", password="ZSBNQSIARMXZDVST")
#
#         message = MIMEText('atukoon 邮件发送测试...', 'plain', 'utf-8')
#         message['From'] = Header("fairly", 'utf-8')  # 发件人的昵称
#         message['To'] = Header("贾文杰", 'utf-8')  # 收件人的昵称
#         message['Subject'] = Header('Python SMTP 邮件测试', 'utf-8')  # 定义主题内容
#         smtp.sendmail(from_addr="classmatejia@126.com", to_addrs="2854794630@qq.com", msg=message.as_string())
#         return HttpResponse("")
