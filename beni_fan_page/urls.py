
"""beni_fan_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views   # Import the views module
from django.urls import include, path

urlpatterns = [
    path('api/', include('api.urls')),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),  # Set root to home view
    path('about/', views.AboutView.as_view(), name='about'),

    path(
        'posts/<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.PostDetailView.as_view(),
        name='post-detail',
    ),
    path(
        'posts/<int:pk>/',
        views.PostDetailView.as_view(),
        name='post-detail'
    ),
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('topics/', views.TopicsListView.as_view(), name='topic-list'),
    path('topics/', views.TopicsView.as_view(), name='topics'),
    path(
        'topics/<slug:slug>/',
        views.TopicsDetailView.as_view(),
        name='topics-detail',
    ),
    path(
        'topics/<int:pk>/',
        views.TopicsDetailView.as_view(),
        name='topics-detail',
    ),
    path('photo_contest/', views.Photo_ContestFormView.as_view(), name='photo_contest'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('terms/', views.terms_and_conditions, name='terms-and-conditions'),
    path('ckeditor/', include('ckeditor_uploader.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
