from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['pk' ,'title', 'date_added', 'is_draft', 'is_published']
