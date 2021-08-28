
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    re_path(r'^add_plus/(?P<product_id>\d+)/$', views.cart_plus, name='cart_plus'),
    re_path(r'^cart_minus/(?P<product_id>\d+)/$', views.cart_minus, name='cart_minus'),
    re_path(r'^ajax_cart_plus/(?P<product_id>\d+)/$', views.ajax_cart_plus, name='ajax_cart_plus')
]