from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import DetailView

from photologue.views import GalleryDetailView
from photologue.views import GalleryListView

from photologue.models import Gallery

"""
class CustomGalleryDetailView(GalleryDetailView):


	The purpose of this custom class is to allow access
	to only a small portion of photos to those not
	logged in.

	def get_queryset(self):
		if not self.request.user.is_authenticated():

			qs = Gallery.public()
			valid_ids = qs.values_list('pk', flat=True)[:3]
			
			return Gallery.objects.filter(pk__in=valid_ids)

			print "not authenticated"
		else:
			print "User authenticated"
"""
			
"""
class CustomGalleryDetailView(GalleryDetailView):

	def get_context_data(self, **kwargs):
		context = super(CustomGalleryDetailView, self).get_context_data(**kwargs)
		if not self.request.user.is_authenticated():
			
			print context
			return context

		else:
			print context
			return context

"""

class CustomGalleryDetailView(GalleryDetailView):
	template_name = 'photologue_custom/gallery_detail.html'
	print "CUSTOM VIEW VIEWED"


class CustomGalleryListView(GalleryListView):
	template_name = 'photologue_custom/gallery_list.html'
	PHOTOLOGUE_GALLERY_SAMPLE_SIZE = 1



			

		
