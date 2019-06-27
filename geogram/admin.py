from django.contrib import admin
from .models import PinDrop,Countries
from leaflet.admin import LeafletGeoAdmin

class PinsAdmin(LeafletGeoAdmin):
	model = PinDrop
	list_display = ['adminpindate','adminusername','adminvisitdate','pinlocation']

	def adminpindate(self, obj):
		return str(obj.pindate)

	def adminvisitdate(self, obj):
		return str(obj.shortvisitdate())

	def adminusername(self, obj):
		return obj.getUsername()

	adminpindate.admin_order_field = 'pindate'
	adminpindate.short_description = 'Pin Date'
	adminvisitdate.short_description = 'Date Visited'
	adminusername.short_description = 'Username'

class CountriesAdmin(LeafletGeoAdmin):
	model = Countries
	list_display = ['name']

admin.site.register(PinDrop, PinsAdmin)
admin.site.register(Countries, CountriesAdmin)
