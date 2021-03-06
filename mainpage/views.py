from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from login.models import User
from .models import Address
from os import sys

def index(request):
	return render(request, 'mainpage/index.html', {'user': request.user})

def my_account(request):
	return render(request, 'mainpage/account.html', {'user': request.user})

def complete_info(request):
	print(request.user.username + str(request.user.id))
	curr_user = User.objects.get(pk=request.user.id)
	try:
		province = request.POST['province']
		city = request.POST['city']
		county = request.POST['county']
		street = request.POST['street']
		consignee = request.POST['consignee']
		consignee_tel = request.POST['consignphone']
		moren = request.POST['moren']
		email = request.POST['email']
		if moren == 'true':
			is_default = True
		else:
			is_default = False
		cellphone = request.POST['phone']
		curr_user.cellphone = cellphone
		curr_user.email = email
		curr_user.save()
		if province!='':
			print(is_default)
			addr = Address(province=province, city=city, county=county, street=street,
				consignee=consignee, consignee_tel=consignee_tel, user_id=curr_user,
				is_default=is_default)
			addr.save()
		return HttpResponse(1)
	except:
		import traceback
		print(traceback.format_exc())
		return HttpResponse(0)

def location(request):
	return render(request, 'mainpage/location.html', {'user': request.user})