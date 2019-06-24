from django.urls import path
from . import views

app_name = 'geogram'

urlpatterns = [
	path('',views.geogramhome,name='gghome'),
	path('logout/',views.logout_request,name='logout'),
	path('pins/',views.pins_request,name='pins_request'),
    path('getpin/',views.getpin,name='getpin'),
]
