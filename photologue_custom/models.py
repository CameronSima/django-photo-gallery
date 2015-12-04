from django.db import models
from taggit.managers import TaggableManager
from photologue.models import Gallery

from django.template.defaultfilters import slugify


class GalleryExtended(models.Model):
	gallery = models.OneToOneField(Gallery, related_name='galleryextended')
	tags = TaggableManager(blank=True)
	objects = models.Manager()
	gallery_name = models.CharField(max_length=50)
	gallery_slug = models.SlugField()

	class Meta:
		verbose_name = u'Extra field'
		verbose_name_plural = u'Extra fields'

	def __str__(self):
		return self.gallery.title

	def save(self, *args, **kwargs):
		
		self.gallery_slug = slugify(self.gallery_name)
		super(GalleryExtended, self).save(*args, **kwargs) 


