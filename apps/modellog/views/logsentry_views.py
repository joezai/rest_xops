from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, filters, viewsets
from common.pagination import StandardResultsSetPagination
from modellog.models import LogsEntry
from modellog.serializers.logsentry_serializers import LogsEntrySerializer
from modellog.filters import LogsEntryFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


class LogsEntryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,  viewsets.GenericViewSet):
    queryset = LogsEntry.objects.order_by('-id')
    serializer_class = LogsEntrySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('id', 'user')
    # 双下滑线表示 跨表查询 一般字段都是外键或者m2m
    search_fields = ('message', 'user__username')
    filterset_class = LogsEntryFilter
    pagination_class = StandardResultsSetPagination

