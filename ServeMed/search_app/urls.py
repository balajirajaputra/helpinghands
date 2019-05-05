from django.conf.urls import url
from . import views

app_name='search_app'

urlpatterns = [
#		url('', views.searchResult, name='searchResult'),
		url(r'^$', views.searchResult, name='searchResult'),

]
