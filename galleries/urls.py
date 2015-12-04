from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings

from galleries import views

urlpatterns = patterns('',
	url(r'^$', views.GalleriesListView.as_view(), name='galleries'),
	url(r'^([-\w\d]+)/$', view=views.galleries_page, name='gallery'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)