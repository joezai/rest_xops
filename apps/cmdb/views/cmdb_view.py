from rest_framework import viewsets,mixins
from ..serializers.cmdb_serializer import DeviceGroupSerializer,DeviceGroupListSerializer,DeviceCreateSerializer
from ..models import DeviceInfo,DeviceGroup
from common.custom import CommonPagination, RbacPermission
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class DeviceGroupViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    '''
    资产分组增删改查
    list:
        获取所有分组
    create:
        新建分组
    retrieve:
        分组详情
    '''
    perms_map = (
    {'*': 'admin'}, {'*': 'devicegroup_all'}, {'get': 'devicegroup_list'}, {'post': 'devicegroup_create'},
    {'put': 'devicegroup_edit'}, {'delete': 'devicegroup_delete'})
    queryset = DeviceGroup.objects.all()
    pagination_class = CommonPagination
    filter_backends = (SearchFilter,)
    search_fields = ('group_name',)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DeviceGroupListSerializer
        return DeviceGroupSerializer

class DeviceInfoViewSet(viewsets.ModelViewSet):
    """
    资产信息表增删改查
    """
    perms_map = (
        {'*': 'admin'}, {'*': 'deviceinfo_all'}, {'get': 'deviceinfo_list'}, {'post': 'deviceinfo_create'},
        {'put': 'deviceinfo_edit'}, {'delete': 'deviceinfo_delete'})
    serializer_class = DeviceCreateSerializer
    queryset = DeviceInfo.objects.all()
    pagination_class = CommonPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("device_type","customer_token","main_ip","idc_location","online_state","testapi_state")
    ordering_fields = ('id',)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (RbacPermission,)