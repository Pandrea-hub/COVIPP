from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from models.vaccine.views import VaccineList, VaccineDetail

urlpatterns = [
    url(r'^vaccine/$', VaccineList.as_view(), name='vaccine'),
    url(r'^vaccine/(?P<pk>[0-9]+)/$', VaccineDetail.as_view(), name='vaccine'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
