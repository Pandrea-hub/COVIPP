from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from models.contagion_type.views import ContagionTypeList, ContagionTypeDetail

urlpatterns = [
    url(r'^contagiontype/$', ContagionTypeList.as_view(), name='contagiontype'),
    url(r'^contagiontype/(?P<pk>[0-9]+)/$', ContagionTypeDetail.as_view(), name='contagiontype'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
