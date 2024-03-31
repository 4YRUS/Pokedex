from django.shortcuts import render,redirect 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import sign_up


def home(request):
	if request.user.is_authenticated:

		return render(request,'home.html',{})
	else:
		return redirect('login')

def user_login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user:
			login(request,user)
			return redirect('home')
		else:
			return redirect('login')
	return render(request,'login.html',{})

def user_logout(request):
	logout(request)
	return redirect('login')

def register(request):
	if request.method=='POST':
		form=sign_up(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'User Created Succesfully...')
			return redirect('login')
	else:
		form=sign_up()

	return render(request,'register.html',{'form':form})

def search(request,poll_id):
	if request.user.is_authenticated:

		return render(request,'pokemon.html',{'search':poll_id})
	
	return redirect('login')

