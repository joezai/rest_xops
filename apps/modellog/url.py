from rest_framework import routers
from django.urls import include
from django.conf.urls import url

from modellog.views.logsentry_views import LogsEntryViewSet

router = routers.DefaultRouter()
router.register(r'logsentrys', LogsEntryViewSet, base_name='logsentry')


app_name = 'modellog'
urlpatterns = [
    url('', include(router.urls)),
]