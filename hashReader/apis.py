import json
from urllib2 import urlopen
from urllib import urlencode

from django.shortcuts import HttpResponse

def hash_get(request, query):
    count = 5
    query = urlencode({'q': query})
    response = urlopen("http://search.twitter.com/search.json?%s" % query)
    return HttpResponse(response.read())
