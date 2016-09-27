from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import User
import http.client, urllib.parse


# Create your views here.
def index(request):
	return render(request, 'login/index.html')

def authorize(request):
	user_name = request.POST['user_name']
	password = request.POST['user_pwd']
	try:
		user = User.objects.get(name=user_name)
		if user.password != password:
			raise User.DoesNotExist
		else:
			return HttpResponseRedirect(reverse('login:jmp_to_mainpage'))
	except User.DoesNotExist:
		return render(request, 'login/index.html',{
				'error_message': '用户名或密码错误',
			})

def jmp_to_mainpage(request):
	print(request)
	return render(request, 'mainpage/index.html')

def jmp_to_register(request):
	return HttpResponseRedirect(reverse('login:register_page'))

def register_page(request):
	return render(request, 'login/register.html')

def register(request):
	name = request.POST['user_name']
	password = request.POST['user_pwd']
	email = request.POST['user_email']
	cellphone = request.POST['user_phone']
	user = User(name=name, password=password,email=email,cellphone=cellphone)
	user.save()
	return HttpResponseRedirect(reverse('login:index'))