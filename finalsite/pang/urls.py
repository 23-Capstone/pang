from django.urls import path
from . import views

app_name = 'pang'
urlpatterns = [
    # /pang/
    path("", views.index, name="index"),
    path("main/", views.main, name="main"),
]