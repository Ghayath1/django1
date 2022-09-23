from django.contrib import admin

# Register your models here.
from .models import Post
class PostAdmin(admin.ModelAdmin):
    list_display=['title','active','publish_date','author']
    list_filter=['active','author']
    search_fields=['title','content']

admin.site.register(Post,PostAdmin)
