#tests\blog\models\test_post.py
import string

from model_mommy import mommy
import pytest

from blog.models import Comment, Post

#pylint: disable=no-member

pytestmark = pytest.mark.django_db

def test_get_authors_returns_users_who_have_authored_a_post(django_user_model):
    # Create a user
    author = mommy.make(django_user_model)
    # Create a post that is authored by the user
    mommy.make('blog.Post', author=author)
    # Create another user – but this one won't have any posts
    mommy.make(django_user_model)

    assert list(Post.objects.get_authors()) == [author]

def test_question_post_with_most_comments():
    #create a post
    post = mommy.make('blog.Post', title='test', status='PUBLISHED')
    #create comments for the post
    mommy.make('blog.Comment', post=post, _quantity=3)

    assert [{'title': "test", 'comments__count': 3}] == list(Post.objects.return_10_post_with_the_most_comments())
