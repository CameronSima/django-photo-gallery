from django.conf.urls import *
from views import CustomGalleryDetailView, CustomGalleryListView


urlpatterns = patterns('',
	url(r'^gallery/(?P<slug>[\-\d\w]+)/$',
			CustomGalleryDetailView.as_view(), name='pl-custom-gallery'),

	url(r'^gallerylist/$', 
		CustomGalleryListView.as_view(), name='pl-custom-gallery-list'),

)