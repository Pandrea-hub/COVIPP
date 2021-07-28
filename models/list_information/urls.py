from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from models.list_information.views import ListInformationList, ListInformationDetail, CompleteInformationListView

urlpatterns = [
    url(r'^listinformation/$', ListInformationList.as_view(), name='listinformation'),
    url(r'^listinformation/(?P<pk>[0-9]+)/$', ListInformationDetail.as_view(), name='listinformation'),
    url(r'^user/(?P<user_id>.+)/completelistinformation/$', CompleteInformationListView.as_view(), name='completelistinformation'),
]

urlpatterns = format_suffix_patterns(urlpatterns)