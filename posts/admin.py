from django.contrib import admin

from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','category','draft']
    list_filter = ['draft','tags','category']
    search_fields = ['title','tags']


# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)