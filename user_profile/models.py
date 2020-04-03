from django.db import models
from django.utils.text import slugify

# Create your models here.
class PostModel(models.Model):
	author		= models.CharField(max_length=30)
	title  		= models.CharField(max_length=255)
	body  		= models.TextField()
	category  	= models.CharField(max_length=255)
	publish		= models.DateTimeField(auto_now_add=True)
	update  	= models.DateTimeField(auto_now=True)
	slug		= models.SlugField(blank=True, editable=False)

	def save(self):
		self.slug = slugify(self.title)
		super(PostModel, self).save()

	def __str__(self):
		return "{}. {}".format(self.id, self.title)