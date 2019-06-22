from django.contrib import admin
from .models import Blogpost

class BlogpostAdmin(admin.ModelAdmin):
	model = Blogpost
	list_display = ['admintitle',]

	def admintitle(self, obj):
		return str(obj.shortpubdate()) + ' ' + obj.title

	admintitle.admin_order_field = 'pubdate'
	admintitle.short_description = 'Post Details'

admin.site.register(Blogpost, BlogpostAdmin)