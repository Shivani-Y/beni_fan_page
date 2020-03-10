""" test_views.py"""
#from django.test.client import Client
import pytest
pytestmark = pytest.mark.django_db
def test_index_ok(client):
    """ testing to get 200 server response"""
    # Make a GET request to / and store the response object
    # using the Django test client.
    #client = Client()
    response = client.get('/')
    # Assert that the status_code is 200 (OK)
    assert response.status_code == 200

def test_index_404(client):
    """testing to get a 404 response on a wrong get request"""
    response = client.get('/banana')  # Doesn't exist
    assert response.status_code == 404
