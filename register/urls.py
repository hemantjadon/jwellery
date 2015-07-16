from django.conf.urls import url,patterns,include
from .views import *
from django.conf import settings

urlpatterns = patterns('',
 	url(r'^register/$',registration_form),
    url(r'^email_confirmation/(?P<auth_token>[a-zA-Z0-9_.-=$]+)/$',email_confirmation),
    url(r'^hello/$',hello),             
    url(r'login/$',myLogin),
			)