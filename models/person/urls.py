from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from models.person.views import PersonView, PersonDetail

urlpatterns = [
    url(r'^person/$', PersonView.as_view(), name='person'),
    url(r'^person/(?P<pk>[0-9]+)/$', PersonDetail.as_view(), name='person')
]

urlpatterns = format_suffix_patterns(urlpatterns)
