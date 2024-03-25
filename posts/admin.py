from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


from .models import Post, Category, Comment

class PostAdmin(SummernoteModelAdmin):
    list_display = ['title','category','draft']
    list_filter = ['draft','tags','category']
    search_fields = ['title','tags']

    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)