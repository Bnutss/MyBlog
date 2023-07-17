from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_display_links = ['title', 'author']
    search_fields = ('title', 'author')


admin.site.register(Post, PostAdmin)
