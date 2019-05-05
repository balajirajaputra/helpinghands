from django.conf.urls import url
from hhands import views
from django.contrib.auth import views as auth_views

app_name = 'hhands'

urlpatterns = [
#    url(r'^$',views.setup, name='setup'),

    url(r'^drugs',views.DrugsHeaderView.as_view(),name='drugs'),
    url(r'^searchdrugs/(?P<pk>\d+)/',views.DrugsHeaderDetailView.as_view(),name='drugheaderdetails'),
    url(r'^create/$',views.DrugsHeaderCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.DrugsHeaderUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.DrugsHeaderDeleteView.as_view(),name='delete'),
    url(r'^hcps',views.HcpInformationView.as_view(),name='hcps'),
    url(r'^searchhcp/(?P<pk>\d+)/',views.HcpInformationDetailView.as_view(),name='hcpinfodetails'),
    # url(r'^searchhcp_data/(?P<id>\d+)/',views.Hcp_dataDetailView.as_view(),name='hcpdatalist'),

    url(r'^searchdrugs/$',views.searchdrugs),
    url(r'^getimage/$', views.getimage),
    url(r'^searchhcp/$',views.searchhcp),
    # url(r'^searchhcp_data/$',views.searchhcp_data),

    url(r'^login/$',auth_views.LoginView.as_view(template_name='hhands/login.html'),name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'^signup/$',views.signup.as_view(),name='signup'),

]
