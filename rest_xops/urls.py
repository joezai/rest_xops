from django.urls import include
from django.conf.urls import url
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from rest_xops.settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    url(r'^api/rbac/', include('rbac.urls','rbac')),
    url(r'^api/cmdb/', include('cmdb.urls')),
    url('docs/', include_docs_urls()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login', obtain_jwt_token),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^logs/', include('modellog.url'))
]
