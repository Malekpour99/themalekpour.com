from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path("", home_view, name="home"),
    path("<int:pid>", single_view, name="single"),
    path("category/<str:cat_name>", home_view, name="category"),
    path("tag/<str:tag_name>", home_view, name="tag"),
    path("author/<str:author_username>", home_view, name="author"),
    path("search/", search_view, name="search"),
]
