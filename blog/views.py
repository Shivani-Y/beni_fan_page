# blog/views.py

from django.shortcuts import render
from django.contrib.auth import get_user_model
from . import models

# pylint: disable=no-member
def home(request):
    """
    The Blog homepage
    """
    # Get last 3 posts
    latest_posts = models.Post.objects.published().order_by('-published')[:3]
    authors = models.Post.objects.get_authors()
    get_posts = models.Post.objects.return_10_post_with_the_most_comments()[:10]
    get_topics = models.Topic.objects.return_10_topics_with_the_most_post()[:10]
    # Add as context variable "latest_posts"
    context = {
        'authors': authors,
        'latest_posts': latest_posts,
        'get_posts': get_posts,
        'get_topics': get_topics
    }
    #render(request, 'blog/home.html', {'message': 'Hello world!'})
    #return render(request, 'blog/home.html', {'message': 'Get to know Beni!'})
    return render(request, 'blog/home.html', context)
