from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from models.gender.views import GenderList, GenderDetail

urlpatterns = [
    url(r'^gender/$', GenderList.as_view(), name='gender'),
    url(r'^gender/(?P<pk>[0-9]+)/$', GenderDetail.as_view(), name='gender'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
