# blog/views.py

from django.shortcuts import render
#from models import Post, Comment
from . import models
# pylint: disable=no-member
def home(request):
    """
    The Blog homepage
    """
    # Get last 3 posts
    latest_posts = models.Post.objects.published().order_by('-published')[:1]
    # Add as context variable "latest_posts"
    context = {'latest_posts': latest_posts}
    #render(request, 'blog/home.html', {'message': 'Hello world!'})
    #return render(request, 'blog/home.html', {'message': 'Get to know Beni!'})
    return render(request, 'blog/home.html', context)
