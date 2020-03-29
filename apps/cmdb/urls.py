from django.urls import include
from django.conf.urls import url
from cmdb.views import dict,scan,asset,connection,business,group,label
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'dicts', dict.DictViewSet, base_name="dicts")
router.register(r'scan/devices', scan.DeviceScanInfoViewSet, base_name="scan_devices")
router.register(r'devices', asset.DeviceInfoViewSet, base_name="devices")
router.register(r'connections', connection.ConnectionInfoViewSet, base_name="connections")
router.register(r'businesses', business.BusinessViewSet, base_name="businesses")
router.register(r'groups', group.DeviceGroupViewSet, base_name="groups")
router.register(r'labels', label.LabelViewSet, base_name="labels")
app_name = 'cmdb'

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'dict/tree/', dict.DictTreeView.as_view(), name='dict_tree'),
    url(r'scan/setting/', scan.ScanSettingView.as_view(), name='scan_setting'),
    url(r'scan/excu/', scan.ScanExcuView.as_view(), name='scan_excu'),
    url(r'device/list/', asset.DeviceListView.as_view(), name='device_list'),
]
