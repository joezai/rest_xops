from rest_framework.response import Response
from apps.utils.geoipcheck import IPcheckMixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import  mixins,viewsets
class IPcheckViewset(IPcheckMixins, mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    def list(self, request, *args, **kwargs):
        ipaddress = request.GET.get('ipaddress')
        try:
            result = IPcheckMixins.getipinfo(ipaddress)
            return Response(result,status.HTTP_200_OK)
        except:
            return Response({'msg': 'IPADDRESS NOT FOUND'}, status.HTTP_400_BAD_REQUEST)