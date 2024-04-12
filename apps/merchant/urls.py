from django.urls import path

from apps.merchant.views import *

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('registercountemail', MerchantEmailCounter.as_view()),
    path('login', MeLoginView.as_view()),
    path('index', MeIndexView.as_view()),
    path('setupshop', SetupshopView.as_view()),
    path('logout', MeLogoutView.as_view()),
    path('alterinfo', AlterInfoView.as_view()),
    path('isopen', MerchantModalOpen.as_view()),
    path("desc", DescView.as_view())

]
