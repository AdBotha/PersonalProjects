from django.shortcuts import render, get_object_or_404
from .models import Blogpost

def home(request):
	blogposts = Blogpost.objects.order_by('-pubdate')
	return render(request,'blog/home.html',{'posts':blogposts})

def postdetails(request,post_id):
	post = get_object_or_404(Blogpost,pk=post_id)
	return render(request,'blog/post_details.html',{'post':post})