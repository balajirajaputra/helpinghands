from django.conf.urls import url
from shop import views
from django.contrib.auth import views as auth_views


app_name = 'shop'

urlpatterns = [
    url(r'^$', views.allProdCat, name='allProdCat'),
    url(r'^(?P<c_slug>[\w-]+)/$', views.allProdCat, name='products_by_category'),
    url(r'^(?P<c_slug>[\w-]+)/(?P<product_slug>[\w-]+)/$', views.ProdCatDetail, name='ProdCatDetail'),


]
