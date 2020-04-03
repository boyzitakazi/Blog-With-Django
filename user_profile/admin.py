from django.contrib import admin
from .models import PostModel
# Register your models here.
class AdminPost(admin.ModelAdmin):
	readonly_fields = ['slug',]

admin.site.register(PostModel, AdminPost)
