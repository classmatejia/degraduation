from django.urls import path

from apps.verifications.views import *

urlpatterns = [
    # path("sendemail", SendEmailView.as_view()),
    path("<uuid:uuid>", CaptchaView.as_view()),

]
