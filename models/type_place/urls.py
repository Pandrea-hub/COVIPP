from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from models.type_place.views import TypePlaceList, TypePlaceDetail

urlpatterns = [
    url(r'^typeplace/$', TypePlaceList.as_view(), name='typeplace'),
    url(r'^typeplace/(?P<pk>[0-9]+)/$', TypePlaceDetail.as_view(), name='typeplace'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
