"""importing and registring model in django admin"""
# blog/admin.py
from django.contrib import admin
from . import models

# Register the `Post` model
admin.site.register(models.Post)
