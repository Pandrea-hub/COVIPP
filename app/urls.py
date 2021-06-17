from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from rest_framework.authtoken import views
from rest_framework.schemas.coreapi import AutoSchema
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from django.conf.urls.static import static
from models.person.serializers import CustomAuthToken, CustomAuthLogout

router = routers.DefaultRouter()

# Admin
urlpatterns = [
    url('admin/', admin.site.urls),
]

# Auth
urlpatterns += [
    url(r'^api/v1/auth', include('rest_framework.urls', namespace="rest_framework")),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api/v1/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/login/', CustomAuthToken.as_view()),
    url(r'^api/v1/logout/', CustomAuthLogout.as_view()),
    url(r'^api/v1/', include('models.person.urls')),
]

# Models
urlpatterns += [
    url(r'^api/v1/', include('models.cases.urls')),
    url(r'^api/v1/', include('models.contagion_type.urls')),
    url(r'^api/v1/', include('models.gender.urls')),
    url(r'^api/v1/', include('models.list_information.urls')),
    url(r'^api/v1/', include('models.place.urls')),
    url(r'^api/v1/', include('models.rol.urls')),
    url(r'^api/v1/', include('models.type_place.urls')),
    url(r'^api/v1/', include('models.vaccine.urls')),
]

urlpatterns += router.urls
