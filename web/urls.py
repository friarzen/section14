"""
Url definition file to redistribute incoming URL requests to django
views. Search the Django documentation for "URL dispatcher" for more
help.

"""
from django.conf.urls import url, include

# default evennia patterns
from evennia.web.urls import urlpatterns

# eventual custom patterns
custom_patterns = [
    url(r'^wiki/', include('evennia_wiki.urls', namespace='wiki')),
]

# this is required by Django.
urlpatterns = custom_patterns + urlpatterns
