from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from cart.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from cart import views
from django.conf.urls import url

app_name='cart'

urlpatterns = [

	url(r'^add/(?P<product_id>[\w-]+)/$', views.add_cart, name='add_cart'),
	url(r'^$',views.cart_detail, name='cart_detail'),
	url(r'^remove/(?P<product_id>[\w-]+)/$', views.cart_remove, name='cart_remove'),
	url(r'^full_remove/(?P<product_id>[\w-]+)/$', views.full_remove, name='full_remove'),
	#r'^update/(?P<pk>\d+)/$
	#url(r'^add/<int:product_id>/$', views.add_cart, name='add_cart'),


    #url(r'^(?P<c_slug>[\w-]+)/$', views.allProdCat, name='products_by_category'),

	#path('add/<int:product_id>/', views.add_cart, name='add_cart'),
	#path('', views.cart_detail, name='cart_detail'),
	#path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
	#path('full_remove/<int:product_id>/', views.full_remove, name='full_remove'),

]
