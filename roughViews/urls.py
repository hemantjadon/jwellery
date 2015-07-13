from django.conf.urls import url,patterns,include
from roughViews.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
				url(r'^$',initialPage,name='initial_page'),
				url(r'^jwellery/$',jwelleryPage,name='jwellery_page'),
			)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)