from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from models.place.views import PlaceList, PlaceDetail, PlaceByPlaceType

urlpatterns = [
    url(r'^place/$', PlaceList.as_view(), name='place'),
    url(r'^place/(?P<pk>[0-9]+)/$', PlaceDetail.as_view(), name='place'),
    url(r'^type_place/(?P<type_place_id>.+)/place/$', PlaceByPlaceType.as_view(), name='placebytypeplace'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
