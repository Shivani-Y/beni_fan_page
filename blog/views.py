# blog/views.py

from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView, FormView, ListView
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
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

    # pylint: disable=undefined-variable

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

class ContactFormView(CreateView):
    model = models.Contact
    success_url = reverse_lazy('home')
    fields = [
        'first_name',
        'last_name',
        'email',
        'message',
    ]

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you! Your message has been sent.'
        )
        return super().form_valid(form)

class Photo_ContestFormView(CreateView):
    model = models.Photo_Contest
    success_url = reverse_lazy('home')
    fields = [
        'first_name',
        'last_name',
        'email',
        'image',
    ]

    def upload_pic(self, request):
        if request.method == 'POST':
            form = photo_contest_form(request.POST, request.FILES)
            if form.is_valid():
                m = photo_contest.objects.get(pk=course_id)
                m.model_pic = form.cleaned_data['image']
                m.save()
                return HttpResponse('image upload success')
        return HttpResponseForbidden('allowed only via POST')

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you! Your image has been submitted.'
        )
        return super().form_valid(form)
