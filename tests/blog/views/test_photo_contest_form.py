# tests/blog/views/test_contact_form.py

import pytest
from io import BytesIO
from PIL import Image
from django.core.files.base import File
from django.core.files.images import ImageFile
from blog.models import Photo_Contest

pytestmark = pytest.mark.django_db

# pylint: disable=no-member
def test_post_contest_form_redirect(client, settings, tmpdir):
    # Set media root to a pytest temporary dir
    settings.MEDIA_ROOT = tmpdir
    # Create an image in memory and save to a file buffer
    image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
    file = BytesIO()
    image.save(file, 'png')
    file.name = 'pytest.png'
    file.seek(0)
    data = {
        'first_name': 'George',
        'last_name': 'Costanza',
        'email': 'gcostanza@vandelay.com',
        'image': file
    }

    response = client.post('/photo_contest/', data)
    assert response.status_code == 302
    assert response.url == '/'  # Home

def test_post_contest_form_saves_data(client, settings, tmpdir):
    # Set media root to a pytest temporary dir
    settings.MEDIA_ROOT = tmpdir
    # Create an image in memory and save to a file buffer
    image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
    file = BytesIO()
    image.save(file, 'png')
    file.name = 'pytest.png'
    file.seek(0)
    data = {
        'first_name': 'George',
        'last_name': 'Costanza',
        'email': 'gcostanza@vandelay.com',
        'image': file
    }
    client.post('/photo_contest/', data)
    obj = Photo_Contest.objects.get()
    assert obj.first_name == data['first_name']
    assert obj.last_name == data['last_name']
    assert obj.email == data['email']
    assert obj.image == data['image']

def test_contest_invalid_submission(client):
    data = {'first_name': 'buzz'}
    response = client.post('/photo_contest/', data)
    assert response.status_code != 302
    assert Photo_Contest.objects.exists() is False
