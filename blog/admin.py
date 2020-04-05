"""importing and registring model in django admin"""
# blog/admin.py
from django.contrib import admin
#from models import Comment
from . import models
from .models import Comment

class ExsistingCommentInline(admin.TabularInline):
    """creating inline for comments"""
    extra = 0
    model = Comment
    #fields = ["name", "email", "text", "approved"]
    readonly_fields = ["name", "email", "text"]

    #def exsisting(self, request):
        #return False
    def has_add_permission(self, request, obj=None):
        return False

class NewCommentInline(admin.TabularInline):
    """creating inline for comments"""
    extra = 0
    model = Comment
    fields = ["name", "email", "text", "approved"]
    #readonly_fields = ["name", "email", "text"]
    def has_add_permission(self, request, obj=None):

        return True

# Register the `Post` model
class PostAdmin(admin.ModelAdmin):
    """customising post model view"""
    list_display = ('title', 'author', 'created', 'updated')
    #defining how to search on the page
    search_fields = ('title', 'author__username', 'author__first_name', 'author__last_name')
    #we can now filter on the basis of status all, draft or published
    list_filter = (
        'status',
        'topics',
    ) #admin.RelatedOnlyFieldListFilter
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        ExsistingCommentInline,
        NewCommentInline
    ]

    #def author(self, obj):#for list_display
        #return obj.author

    #def title(self, obj):#for list_display
        #return obj.title
class CommentAdmin(admin.ModelAdmin):
    """customising post model view"""
    list_display = (
        'name',
        'text',
        'created',
        'updated',
        'approved',
    )
    #defining how to search on the page
    search_fields = (
        'text',
    )
    #we can now filter on the basis of approved or not
    list_filter = (
        'approved',
    )

class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'last_name',
        'first_name',
        'submitted'
    )
    # Make these fields read-only in the admin
    readonly_fields = (
        'first_name',
        'last_name',
        'email',
        'message',
        'submitted'
    )

class Photo_ContestAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'last_name',
        'first_name',
        'photo_submitted'
    )
    # Make these fields read-only in the admin
    readonly_fields = (
        'first_name',
        'last_name',
        'email',
        'image',
        'photo_submitted'
    )
    list_filter = (
        'photo_submitted',
    )
class HomeAdmin(admin.ModelAdmin):
    display = 'home_image'
# Register the `Post` model
admin.site.register(models.Post, PostAdmin)
# Register the `Comment` model
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.Photo_Contest, Photo_ContestAdmin)
admin.site.register(models.Home, HomeAdmin)
