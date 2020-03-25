# blog/context_processors.py

from . import models


def base_context(request):
    authors = models.Post.objects.published() \
        .get_authors() \
        .order_by('first_name')
    get_topics = models.Topic.objects.return_10_topics_with_the_most_post()[:10]


    return {'authors': authors,'get_topics': get_topics}
