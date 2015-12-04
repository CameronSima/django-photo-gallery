from django.shortcuts import render, get_list_or_404
#from django.views.generic.list import ListView
from photologue.views import GalleryListView

from photologue.models import Photo, Gallery
from photologue_custom.models import GalleryExtended

class GalleryListView(GalleryListView):
	template_name = 'galleries.html'
	
	"""
	return only one object for each
	unique gallery_name field
	"""
	
	queryset = Gallery.objects.order_by('galleryextended__gallery_name'
							 ).distinct('galleryextended__gallery_name')
	#queryset = Gallery.objects.on_site().is_public()

def galleries_page(request, slug):
	galleries_page = get_list_or_404(Gallery.objects.on_site().is_public()
										.filter(galleryextended__girl_slug=slug))
	return render(request, 'galleriespage.html', {'object_list': galleries_page})

	"""
def unique_galleries(request, tag):
	galleries = get_list_or_404(Gallery.objects.on_site().is_public(),
								Gallery__tag=tag)
	return render(request, 'girlspage.html', {'galleries': galleries})
	"""