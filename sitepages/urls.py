from django.urls import path
from . import views

app_name = 'sitepages'

urlpatterns = [
	path('about/',views.about,name='about'),
]