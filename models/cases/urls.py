from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from models.cases.views import CasesList, CasesDetail, CasesByContagionType,CasesByPerson,CasesBySymptom,CasesByContagion,CasesByPersonAndCase, CaseContagionByPersonAndCase


urlpatterns = [
    url(r'^cases/$', CasesList.as_view(), name='cases'),
    url(r'^cases/(?P<pk>[0-9]+)/$', CasesDetail.as_view(), name='cases'),
    url(r'^contagion_type/(?P<contagion_type_id>.+)/cases/$', CasesByContagionType.as_view(), name='casesbycontagiontype'),
    url(r'^person/(?P<person_id>.+)/cases/$', CasesByPerson.as_view(), name='casesbyperson'),
    url(r'^person/(?P<person_id>.+)/symptomcases/$', CasesBySymptom.as_view(), name='casesbysymptom'),
    url(r'^person/(?P<person_id>.+)/contagioncases/$', CasesByContagion.as_view(), name='casesbycontagion'),
    url(r'^person/(?P<person_id>.+)/cases/(?P<cases_id>.+)/case/$', CasesByPersonAndCase.as_view(), name='casesbypersonandvcase'),
    url(r'^person/(?P<person_id>.+)/contagioncases/(?P<cases_id>.+)/case/$', CaseContagionByPersonAndCase.as_view, name= 'casecontagionbypersonandcase')
]

urlpatterns = format_suffix_patterns(urlpatterns)
