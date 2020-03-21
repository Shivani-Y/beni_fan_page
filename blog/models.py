"""Creating models for the app"""
from django.conf import settings  # Imports Django's loaded settings
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Count
# Create your models here.

class TopicQuerySet(models.QuerySet):
    """query set for topic object"""
    def return_10_topics_with_the_most_post(self):
        """
        Return topics containing the most posts. sorted by comment counts
        """
        #all_topics = self.all() #filter(blog_posts__status='PUBLISHED')
        result = self.values('name').filter(blog_posts__status='published').annotate(Count('blog_posts__title')).order_by('-blog_posts__title__count')
        #annotate(Count('blog_posts__title'))

        #result = published_post.values('topics').annotate(Count('title')).order_by('-title__count')
        return result

class Topic(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True  # No duplicates!
    )
    objects = TopicQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class PostQuerySet(models.QuerySet):
    """query set for post object"""

    def published(self):
        """display only published post"""
        return self.filter(status=self.model.PUBLISHED)

    def drafts(self):
        """display only draft post"""
        return self.filter(status=self.model.DRAFT)

    def get_authors(self):
        """Get the users who are authors of this queryset"""
        User = get_user_model()
        return User.objects.filter(blog_posts__in=self).distinct()

    def return_10_post_with_the_most_comments(self):
        """
        Return the Post object containing the most comments. sorted by comment counts
        """
        one_result = self.filter(status=self.model.PUBLISHED)
        result = one_result.values('title').annotate(Count('comments')).order_by('-comments__count')
        return result

class Post(models.Model):
    """
    Represents a blog post
    """
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [(DRAFT, 'Draft'), (PUBLISHED, 'Published')]
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each savenote
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # The Django auth user model
        on_delete=models.PROTECT,  # Prevent posts from being deleted
        related_name='blog_posts',  # "This" on the user model
        null=False
    )
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published'
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=10,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible'
    )
    slug = models.SlugField(
        null=False,
        unique_for_date='published',  # Slug is unique for publication date
    )
    topics = models.ManyToManyField(
        Topic,
        related_name='blog_posts'
    )
    objects = PostQuerySet.as_manager()

    class Meta:
        """sorting the posts in reverse"""
        # Sort by the `created` field. The `-` prefix
        # specifies to order in descending/reverse order.
        # Otherwise, it will be in ascending order.
        ordering = ['-created']

    def __str__(self):
        return self.title

class CommentQuerySet(models.QuerySet):
    def approved(self):
        self.filter(approved=True)



class Comment(models.Model):
    """
    Represents a comments section
    """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=254, null=False)
    text = models.CharField(max_length=255, null=False)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save
    objects = CommentQuerySet.as_manager()
    class Meta:
        """sorting the posts in reverse"""
        ordering = ['-created']



    def __str__(self):
        return self.name
