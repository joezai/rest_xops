from django.urls import include
from rest_framework import routers
from django.conf.urls import url
from .views import cmdb_view
from .views import geoip_view
from .views.geoip_view import IPcheckViewset
router = routers.DefaultRouter()
### 分组信息url
router.register(r'devicegroups', cmdb_view.DeviceGroupViewSet, basename="devicegroups")
### 资产信息url
router.register(r'deviceinfos', cmdb_view.DeviceInfoViewSet, basename="deviceinfos")
router.register(r'geoipcheck', geoip_view.IPcheckViewset, basename="geoipcheck")
app_name = 'cmdb'
urlpatterns = [
    url(r'', include(router.urls)),
]