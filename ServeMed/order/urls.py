from django.conf.urls import url
from order import views

app_name='order'

urlpatterns = [
	# path('thanks/<int:order_id>/', views.thanks, name='thanks'),
	# path('history/', views.orderHistory, name='order_history'),
	# path('<int:order_id>/', views.viewOrder, name='order_detail'),

	url(r'^thanks/(?P<order_id>[\w-]+)/$', views.thanks, name='thanks'),
	url(r'^history/$',views.orderHistory, name='orderHistory'),
	url(r'^(?P<order_id>[\w-]+)/$', views.viewOrder, name='order_detail'),

]
