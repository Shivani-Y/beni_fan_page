# bEni_fan_page/views.py
"""adding text to my bolg"""
from django.http import HttpResponse


def index(request):
    """adding text to my page"""
    return HttpResponse("Hello world! Welcome to Beni's Fan Page")
