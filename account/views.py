from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

# def signup(request):

# 	return render(request,'signup.html')

def signup(request):
	if request.method=='GET':
		return render(request,'signup.html')
	elif request.method=='POST':
		user_name=request.POST['UserName']
		password1=request.POST['Password']
		password2=request.POST['PasswordAgain']
		try:
			User.objects.get(username=user_name)
			return render(request,'signup.html',{'用户名错误':'该用户名已存在'})
		except User.DoesNotExist:
			if password1==password2:
				User.objects.create_user(username=user_name,password=password1)
				return redirect('主页')
			else:
				return render(request,'signup.html',{'密码错误':'两次输入的密码不一致'})


def login(request):
	if request.method=='GET':
		return render(request,'login.html')
	elif request.method=='POST':
		user_name=request.POST['UserName']
		pass_word=request.POST['Password']
		user=auth.authenticate(username=user_name,password=pass_word)
		if user is None:
			return render(request,'login.html',{'登录错误':'用户名或密码错误'})
		else:
			auth.login(request,user)
			return redirect('主页')

def logout(request):
	if request.method=='POST':
		auth.logout(request)
		return redirect('主页')