"""importing and registring model in django admin"""
# blog/admin.py
from django.contrib import admin
from . import models

# Register the `Post` model
class PostAdmin(admin.ModelAdmin):
    """customising post model view"""
    list_display = (
        'title',
        'author',
        'created',
        'updated',
    )
    #defining how to search on the page
    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )
    #we can now filter on the basis of status all, draft or published
    list_filter = (
        'status',
    )
    prepopulated_fields = {'slug': ('title',)}

class CommnetAdmin(admin.ModelAdmin):
    """customising post model view"""
    list_display = (
        'name',
        'text',
        'approved',
        'created',
        'updated',
    )
    #defining how to search on the page
    search_fields = (
        'text',
    )
    #we can now filter on the basis of
    list_filter = (
        'status',
    )

# Register the `Post` model
admin.site.register(models.Post, PostAdmin)
# Register the `Comment` model
admin.site.register(models.Comment, PostAdmin)
