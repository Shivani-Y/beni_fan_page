# tests/api/views/test_comments.py

from django.urls import reverse_lazy
from model_mommy import mommy
import pytest


pytestmark = pytest.mark.django_db

URL = reverse_lazy('api:comment-list')


def test_url():
    assert URL == '/api/comments/'

def test_filtering_by_post(client):
    drf_post = mommy.make('blog.Post')
    comment = mommy.make('blog.Comment', post=drf_post)
    # Unrelated comment
    mommy.make('blog.Comment')

    response = client.get(URL, data={'post': drf_post.pk})

    # Compare the ID field
    expected_ids = [comment.pk]
    result_ids = [obj['id'] for obj in response.json()]

    assert expected_ids == result_ids

def test_invalid_post_value(client):
    response = client.get(URL, data={'post': 'THIS IS NOT AN INT!'})
    assert response.status_code == 200

def test_post_new_comment(client):
    post = mommy.make('blog.Post')
    data = {
        'post': post.pk,
        'name': 'Babu Bhatt',
        'email': 'babu@dreamcafe.com',
        'text': 'This was a very good post. Very good.',
    }
    response = client.post(URL, data=data)
    assert response.status_code == 201
