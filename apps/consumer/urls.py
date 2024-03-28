from django.urls import path

from apps.consumer.views import *

urlpatterns = [
    path("register", RegisterView.as_view()),
    path("login", LoginView.as_view()),
    path("index", IndexView.as_view()),
    path("registercountemail", ConsumerEmailCounter.as_view()),
    path("logout", LogoutView.as_view()),

]
