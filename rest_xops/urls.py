from django.urls import include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^api/rbac/', include('rbac.urls','rbac')),
    url(r'^api/cmdb/', include('cmdb.urls')),
    url('docs/', include_docs_urls()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login', obtain_jwt_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
