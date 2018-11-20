from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.

def product_list(request):
	return render(request,'product_list.html')

@login_required
def publish(request):
	if request.method=='GET':
		return render(request,'publish.html')
	elif request.method=='POST':
		title =request.POST['Title']
		url   =request.POST['APPLink']
		intro =request.POST['Introduction']
		try:
			icon  =request.FILES['APPIcon']
			image =request.FILES['Image']

			product=Product()
			product.title=title
			product.url=url
			product.intro=intro
			product.icon=icon
			product.image=image

			product.pub_date=timezone.datetime.now()
			product.hunter=request.user

			product.save()

			return redirect('主页')
			
		except Exception as err:
			return render(request,'publish.html',{'图片上传错误':'请上传图片'})

		
