from django.urls import path, reverse_lazy
from .views import *

app_name = "accounts"

urlpatterns = [
    path("login/", login_view, name="login"),
]
