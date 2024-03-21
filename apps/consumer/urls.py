from django.urls import path

from apps.consumer.views import *

urlpatterns = [
    path("register", RegisterView.as_view()),
    path("login", LoginView.as_view()),
    path("registercountname", ConsumerCounter.as_view()),

]