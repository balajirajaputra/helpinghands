"""ServeMed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from hhands import views

from hhands.views import index, ChartData, index_TIBar, BarChart

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^home',views.home, name='home'),
    url(r'^setup',views.setup, name='setup'),
    url(r'^customerlogin',views.customerlogin, name='customerlogin'),
    url(r'^physicians',views.physicians, name='physicians'),
    url(r'^dashboard',index_TIBar.as_view(), name='dashboard'),
    url(r'^index_TIBar',index.as_view(), name='index_TIBar'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^api/chart1/data/$', BarChart.as_view()),
    url(r'^checkout',views.CheckoutView.as_view(), name='checkout'),

    #url(r'^index_TIBar',views.index_TIBar, name='index_TIBar'),
    url(r'^data/Med',views.Med, name='Med'),
    url(r'^data/us',views.usdata, name='usdata'),
    url(r'^settings',views.customersettings, name='settings'),
    url(r'^enrollconfirmation',views.enrollconfirmation, name='enrollconfirmation'),
    url(r'^InformationSaved',views.InformationSaved, name='InformationSaved'),
    url(r'^HCPInfo',views.PhysicianInformation, name='PhysicianInformation'),
    url(r'^admin/', admin.site.urls),
    url(r'^base',views.base, name='base'),
    url(r'^hhands/',include('hhands.urls',namespace='hhands')),
    url(r'hhands/',include('django.contrib.auth.urls')),
    url(r'^test/$',views.testpage.as_view(), name='test'),
    url(r'^thanks/$',views.thankspage.as_view(), name='thanks'),

    url(r'^shop/',include('shop.urls')),
    url(r'^search/',include('search_app.urls')),
    url(r'^cart/',include('cart.urls')),
    url(r'^order/',include('order.urls')),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
