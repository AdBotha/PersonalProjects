from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def geogramlogin(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('geogram:gghome')
		else:
			return render(request,'accounts/login.html',{'error':'Username or Password is incorrect!'})
	else:
		return render(request,'accounts/login.html')

def geogramsignup(request):
	if request.method == 'POST':
		if 	request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request,'accounts/signup.html',{'error':'Username is already taken.'})
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'],first_name=request.POST['firstname'],last_name=request.POST['lastname'])
				login(request,user)
				return redirect('geogram:gghome')
		else:
			return render(request,'accounts/signup.html',{'error':'Passwords do not match'})
	else:
		return render(request,'accounts/signup.html')
