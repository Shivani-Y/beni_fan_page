# blog/views.py

from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import View
from django.shortcuts import get_object_or_404
from . import models

# pylint: disable=no-member

class HomeView(TemplateView):
    """
    The Blog homepage
    """
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        # Get the parent context
        context = super().get_context_data(**kwargs)

        # Get last 3 posts
        latest_posts = models.Post.objects.published().order_by('-published')[:3]
        get_posts = models.Post.objects.return_10_post_with_the_most_comments()[:10]
# Update the context with our context variables
        context.update({
            'latest_posts': latest_posts,
            'get_posts': get_posts,
        })
        #render(request, 'blog/home.html', {'message': 'Hello world!'})
        #return render(request, 'blog/home.html', {'message': 'Get to know Beni!'})
        return context

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class TopicsView(TemplateView):
    template_name = 'blog/topics.html'

class PostsView(TemplateView):
    template_name = 'blog/posts.html'

class ContactView(TemplateView):
    template_name = 'blog/contact.html'

def terms_and_conditions(request):
    return render(request, 'blog/terms_and_conditions.html')

class PostListView(ListView):
    model = models.Post
    context_object_name = 'posts'
    queryset = models.Post.objects.published().order_by('-published')

class PostDetailView(DetailView):
    model = models.Post
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset().published()

        # If this is a `pk` lookup, use default queryset
        if 'pk' in self.kwargs:
            return queryset

        # Otherwise, filter on the published date
        return queryset.filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )

class TopicsListView(ListView):
    model = models.Topic
    context_object_name = 'all_topics'

class TopicsDetailView(DetailView):
    model = models.Topic
    context_object_name = 'all_topics'

    def get_context_data(self, **kwargs):
        context = super(TopicsDetailView, self).get_context_data(**kwargs)
        context['post_list'] = models.Post.objects.filter(topics=self.get_object()).published()
        return context
