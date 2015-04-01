from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponse , Http404
from django.template import Context
from django.template.loader import get_template
from django.template import RequestContext	
from Teachers_Portal_App.forms import FormatForm
from Teachers_Portal_App.models import Format
from django.db import models

def main_page(request):
	return render_to_response('main_page.html',{ 'user': request.user,})
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')	
def upload_paper(request):
	if request.method == 'POST':
		form = FormatForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response('registration/register_success.html',{'form':form})
	else:
		form=FormatForm()
	return render_to_response('registration/upload.html',{'form':form}, context_instance=RequestContext(request))

def user_page(request):
	data=Format.objects.get(username="request.user.username")
	return render_to_response('user_page.html',{ 'user': request.user,})