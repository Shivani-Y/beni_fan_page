"""
Queries for assignment
"""
from django.contrib.auth import get_user_model
from django.db.models import Q, Count
from django.apps import apps
from blog.models import Post, Comment
# pylint: disable=C0103
User = get_user_model()
# pylint: disable=no-member
def question_1_return_active_users():
    """
    Return the results of a query which returns a list of all
    active users in the database.
    """
    #works
    result = User.objects.filter(is_active=True)
    return result

def question_2_return_regular_users():
    """
    Return the results of a query which returns a list of users that
    are *not* staff and *not* superusers
    """
    #works
    result = User.objects.filter(is_staff=False, is_superuser=False)
    return result

def question_3_return_all_posts_for_user(user):
    """
    Return all the Posts authored by the user provided. Posts should
    be returned in reverse chronological order from when they
    were created.
    """
    #works
    result = Post.objects.filter(author__username=user).order_by('-created')
    return result

def question_4_return_all_posts_ordered_by_title():
    """
    Return all Post objects, ordered by their title.
    """
    #works
    result = Post.objects.order_by('title')
    return result

def question_5_return_all_post_comments(post):
    """
    Return all the comments made for the post provided in order
    of last created.
    """
    result = Comment.objects.filter(post__title=post).order_by('-created')
    return result

def question_6_get_approved_comments_from_queryset():
    """
    Implement a queryset method on the Comment model called
    `approved` which only returns comments which have approved
    set to `True`. Do not modify the code in this function – make the
    test pass.
    """
    Comment = apps.get_model('blog', 'Comment')
    return Comment.objects.approved()

def question_7_text_search_post_text(expression):
    """
    Using the `expression` argument, return all posts containing
    this expression in their content or title. Make the query
    case-insensitive
    """
    #works
    result = Post.objects.filter(Q(content__icontains=expression) | Q(title__icontains=expression))
    return result

def question_8_return_the_post_with_the_most_comments():
    """
    Return the Post object containing the most comments in
    the database. Do not concern yourself with approval status;
    return the object which has generated the most activity.
    """
    #works
    one_result = Post.objects.annotate(Count('comments')).order_by('comments')[:1]
    sec_result = list(one_result)
    for i in sec_result:
        return i

def question_9_create_a_comment(post):
    """
    Create and return a comment for the post object provided.
    """
    result = Post.objects.get(pk=post).create()
    return result

def question_10_set_approved_to_false(comment):
    """
    Update the comment record provided and set approved=False
    """
    result = Comment.objects.filter(text=comment).update(approved=False)
    return result

def question_11_delete_post_and_all_related_comments(post):
    """
    Delete the post object provided, and all related comments.
    """
    filtered_result = Post.objects.filter(post=post)
    return filtered_result.delete()
