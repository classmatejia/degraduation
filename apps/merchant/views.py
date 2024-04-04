import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django_redis import get_redis_connection
from apps.merchant.models import Merchant
from apps.shop.models import Shop, Goods


def check_login(func):
    """检查用户是否登录没有则重定向到登陆页面"""

    def check_log(self, request):
        if request.session.get('merchant', None):
            return func(self, request)
        else:
            return redirect('/merchant/login')

    return check_log


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
        request.session['merchant'] = me.email
        response.set_cookie('mesessionid', hash(password), max_age=3600 * 24 * 15)
        return response


class MeLogoutView(View):

    def delete(self, request):
        del request.session["merchant"]
        response = JsonResponse({'code': 200,
                                 'errmsg': 'ok'})
        return response


class AlterInfoView(View):
    @check_login
    def put(self, request):
        data = json.loads(request.body.decode('utf-8'))
        alter_name = data.get('alterName')
        alter_address = data.get('alterAddress')
        alter_number = data.get('alterNumber')
        try:
            email = request.session.get('merchant')
            u = Merchant.objects.get(email=email).merchant.all()
            if u:
                user = u[0]
                if alter_name:
                    user.shop_name = alter_name
                    user.save()
                if alter_address:
                    user.addres = alter_address
                    user.save()
                if alter_number:
                    user.phone = alter_number
                    user.save()
                return JsonResponse({'code': 200})
            else:
                return JsonResponse({'code': 202})
        except Merchant.DoesNotExist:
            return JsonResponse({'code': 400})


class MeIndexView(View):

    @check_login
    def get(self, request):

        global mer_shop, mer_shops
        se = request.session.get('merchant', None)  # 拿到session中的邮箱

        try:
            merchant = Merchant.objects.get(email=se)  # 通过邮箱查到商家
            mer_shops = merchant.merchant.all()  # 拿到对应店铺
        except Merchant.DoesNotExist:
            pass
        if mer_shops:
            mer_shop = mer_shops[0]
            store = {'name': mer_shop.shop_name, 'address': mer_shop.adders, 'rating': mer_shop.mark}
        else:
            store = {'name': '你还没有店铺', 'address': '', 'rating': ''}
        queryset = mer_shop.goods.all()

        goods_list = [
            {"item_id": item.id, "name": item.goods_name, "description": item.desc[0:30] + '...',
             "price": item.price} for
            item in queryset]

        context = {
            'store': store,
            'products': goods_list,
        }
        return render(request, 'mcindex.html', context=context)

    @check_login
    def post(self, request):
        json_add = json.loads(request.body.decode('utf-8'))
        goods_name = json_add.get('goods_name')
        goods_desc = json_add.get('goods_desc')
        goods_price = json_add.get('goods_price')
        email = request.session.get('merchant', None)
        merchant = Merchant.objects.get(email=email)
        shop = merchant.merchant.all()[0]
        Goods.objects.create(
            goods_name=goods_name,
            desc=goods_desc,
            price=goods_price,
            shop=shop)
        return JsonResponse({'code': 200})

    @check_login
    def delete(self, request):
        global mer_shop, mer_shops
        se = request.session.get('merchant', None)  # 拿到session中的邮箱

        try:
            merchant = Merchant.objects.get(email=se)  # 通过邮箱查到商家
            mer_shops = merchant.merchant.all()  # 拿到对应店铺
        except Merchant.DoesNotExist as e:
            pass
        json_dict = json.loads(request.body.decode('utf-8'))
        if mer_shops:
            mer_shop = mer_shops[0]
        try:
            queryset = mer_shop.goods.get(id=json_dict.get('id'))
            queryset.delete()
            return JsonResponse({'code': 200})
        except Exception:
            return JsonResponse({'code': 400})


class SetupshopView(View):
    @check_login
    def post(self, request):
        """开店注册"""
        json_dict = json.loads(request.body.decode('utf-8'))
        print(json_dict)
        store_name = json_dict.get('shop_name')
        store_address = json_dict.get('address')
        contact_number = json_dict.get('phone')
        email = request.session.get('merchant')

        merchant = Merchant.objects.get(email=email)
        try:
            if not merchant.merchant.all():  # 检查有没有店铺，只准有一家店目前
                Shop.objects.create(
                    shop_name=store_name,
                    adders=store_address,
                    phone=contact_number,
                    merchant=merchant  # 关联商家用户对象
                )
                return JsonResponse({'code': 200})
            else:
                return JsonResponse({'code': 202})
        except Exception:
            return JsonResponse({'code': 400})
