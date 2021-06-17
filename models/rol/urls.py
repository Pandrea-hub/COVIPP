from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from models.rol.views import RolList, RolDetail

urlpatterns = [
    url(r'^rol/$', RolList.as_view(), name='rol'),
    url(r'^rol/(?P<pk>[0-9]+)/$', RolDetail.as_view(), name='rol'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
