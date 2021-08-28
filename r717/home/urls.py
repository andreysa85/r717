from django.urls import path, re_path
from .views import home, about, contact, product_deteil,send_mail_office,rating_ajax

urlpatterns = [
	path('', home, name='home'),
	path('about/', about, name='about'),
	path('contact/', contact, name='contact'),
	path('send_mail_office/', send_mail_office, name='send_mail_office'),
	path('home/', home, name='home'),
	path('rating_ajax/', rating_ajax, name='rating_ajax'),
	re_path(r'^product_deteil/(?P<id>[0-9]+)$', product_deteil,name='product_deteil'),
]

