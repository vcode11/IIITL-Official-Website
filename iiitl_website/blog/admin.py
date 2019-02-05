from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'date_added', 'is_draft', 'is_published']
    readonly_fields = ['date_added']
    list_display_links = ['pk', 'title']
    search_fields = ['title']
    list_filter = ['is_draft', 'is_published', 'date_added', 'date_published']


admin.site.register(Post, PostAdmin)
