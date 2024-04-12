from django.urls import path

from apps.consumer.views import *

urlpatterns = [
    path("register", RegisterView.as_view()),
    path("login", LoginView.as_view()),
    path("index", IndexView.as_view()),
    path("registercountemail", ConsumerEmailCounter.as_view()),
    path("logout", LogoutView.as_view()),
    path('category<int:num>', CategoryView.as_view()),
    path('shop<int:num>', ShopView.as_view()),
    path('cart', CartView.as_view()),
    path('comment', CommentView.as_view()),
    path('search', SearchView.as_view()),
    path('personal', PersonalView.as_view())



]
