from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
	path('login/',views.geogramlogin,name='gglogin'),
	path('signup/',views.geogramsignup,name='ggsignup'),
]