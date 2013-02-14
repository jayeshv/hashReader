from django.conf.urls import patterns, include, url

from hashReader.views import root_page
from hashReader.apis import hash_get

urlpatterns = patterns('',
                       (r'^$', root_page),
                       (r'^api/hash_get/(.+)$', hash_get)                       
                       )
