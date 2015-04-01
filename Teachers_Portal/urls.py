from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from Teachers_Portal_App.views import *
import os.path
from django.contrib import admin

urlpatterns = patterns('',
    (r'^$', main_page),
	(r'^logout/$', logout_page),
	(r'^login/$', 'django.contrib.auth.views.login'),
	(r'^admin/', include(admin.site.urls)),
	(r'^upload_paper/$', upload_paper),
	(r'^user_page/$', user_page),
	(r'^registration/register_success/$', TemplateView.as_view(template_name="registration/register_success.html")),
)
