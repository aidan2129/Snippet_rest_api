from django.contrib import admin

from .models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'style', 'owner')
    list_filter = ('language', )
    search_fields = ['title', 'code']

admin.site.register(Snippet, SnippetAdmin)
