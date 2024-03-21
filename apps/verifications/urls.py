from django.urls import path

from apps.verifications.views import *

urlpatterns = [
    path("<uuid:uuid>", CaptchaView.as_view())
]