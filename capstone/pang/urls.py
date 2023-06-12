from django.urls import path
from . import views

app_name = 'pang'
urlpatterns = [
    # /pang/
    path("", views.index, name="index"),
    # /pang/show/
    path("show/", views.show, name="show"),
    # /pang/delete_item/2
    path('show/delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    # /pang/delete_small/2
    path('show/delete_small/<int:smallcategory_id>/', views.delete_small, name='delete_small'),
    # /pang/delete_big/2
    path('show/delete_big/<int:category_id>/', views.delete_big, name='delete_big'),
    # /pang/convert/2
    path('convert/', views.convert, name="convert"),
]
