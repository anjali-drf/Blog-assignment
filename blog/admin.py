from django.contrib import admin
from .models import Blog,Comment
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_datetime', 'tag_list') # add 'tag_list' to display tags in admin
    search_fields = ['title', 'author__username', 'tags__name'] # add tags__name to search by tag name

    def tag_list(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)