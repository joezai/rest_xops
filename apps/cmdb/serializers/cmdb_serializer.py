from rest_framework import serializers
from ..models import DeviceGroup,DeviceInfo
from django.db.models import Q
from rest_framework.validators import UniqueValidator
class DeviceGroupSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(max_length=100,validators=[UniqueValidator(queryset=DeviceGroup.objects.all())])
    class Meta:
        model = DeviceGroup
        fields = ("group_name","groupdesc")
class DeviceCreateSerializer(serializers.ModelSerializer):
    customer = serializers.CharField(required=True,max_length=100, help_text="客户",error_messages={
                                     "blank": "请输入客户名",
                                     "required": "请输入客户名"
                                 })
    customer_token = serializers.CharField(max_length=30, required=True, help_text="商户编码",error_messages={
                                     "blank": "请输入商户编码",
                                     "required": "请输入商户编码"
                                 })
    main_record = serializers.CharField(max_length=100, required=True,help_text="主解析记录",error_messages={
                                     "blank": "请输入主记录",
                                     "required": "请输入主记录"
                                 })
    sub_record = serializers.CharField(max_length=100, required=True, help_text="副解析记录",error_messages={
                                     "blank": "请输入副记录",
                                     "required": "请输入副记录"
                                 })
    cdn_record = serializers.CharField(max_length=100, required=True, help_text="cdn解析记录",error_messages={
                                     "blank": "请输入cdn记录",
                                     "required": "请输入cdn记录"
                                 })
    main_ip = serializers.IPAddressField(required=True, help_text="主ip",error_messages={
                                     "blank": "请输入主ip",
                                     "required": "请输入主ip"
                                 })
    back_ip = serializers.IPAddressField(required=True, help_text="副ip",error_messages={
                                     "blank": "请输入副ip",
                                     "required": "请输入副ip"
                                 })
    apapa_ip = serializers.IPAddressField(required=False,allow_blank=True,allow_null=True,help_text="APAPAip")
    cdn_ip = serializers.IPAddressField(required=False,allow_blank=True, allow_null=True,help_text="CDNip")
    lan_ip = serializers.IPAddressField(read_only=False,allow_blank=True,allow_null=True,help_text='LANip')
    creater = serializers.CharField(max_length=30, required=True, help_text="搭建人",error_messages={
                                     "blank": "请输入创建人",
                                     "required": "请输入创建人"
                                 })
    def validate_custumer_token(self,custumer_token):
        if DeviceInfo.objects.filter(custumer_token=custumer_token).count():
            raise serializers.ValidationError("商户编码已经存在")
        return custumer_token
    def validate_main_ip(self,main_ip):
        if DeviceInfo.objects.filter(~Q(customer_token=self.instance),main_ip=main_ip):
            instance = DeviceInfo.objects.filter(~Q(customer_token=self.instance),main_ip=main_ip)
            raise serializers.ValidationError("该ip和{}客户主ip冲突，请查看".format(instance[0].customer_token))
        if DeviceInfo.objects.filter(back_ip=main_ip):
            instance = DeviceInfo.objects.filter(back_ip=main_ip)
            raise serializers.ValidationError("该ip和{}客户副ip冲突，请查看".format(instance[0].customer_token))
        if DeviceInfo.objects.filter(apapa_ip=main_ip):
            instance = DeviceInfo.objects.filter(apapa_ip=main_ip)
            raise serializers.ValidationError("该ip和{}客户apapaip冲突，请查看".format(instance[0].customer_token))
        if DeviceInfo.objects.filter(cdn_ip=main_ip):
            instance = DeviceInfo.objects.filter(cdn_ip=main_ip)
            raise serializers.ValidationError("该ip和{}客户cdnip冲突，请查看".format(instance[0].customer_token))
        return main_ip
    def validate_back_ip(self,back_ip):
        if DeviceInfo.objects.filter(main_ip=back_ip):
            instance = DeviceInfo.objects.filter(main_ip=back_ip)
            raise serializers.ValidationError("该ip和{}客户主ip冲突，请查看".format(instance[0].customer_token))
        if DeviceInfo.objects.filter(~Q(customer_token=self.instance),back_ip=back_ip):
            instance = DeviceInfo.objects.filter(~Q(customer_token=self.instance),back_ip=back_ip)
            raise serializers.ValidationError("该ip和{}客户副ip冲突，请查看".format(instance[0].customer_token))
        if DeviceInfo.objects.filter(apapa_ip=back_ip):
            instance = DeviceInfo.objects.filter(apapa_ip=back_ip)
            raise serializers.ValidationError("该ip和{}客户apapaip冲突，请查看".format(instance[0].customer_token))
        if DeviceInfo.objects.filter(cdn_ip=back_ip):
            instance = DeviceInfo.objects.filter(cdn_ip=back_ip)
            raise serializers.ValidationError("该ip和{}客户cdnip冲突，请查看".format(instance[0].customer_token))
        return back_ip
    def validate_apapa_ip(self,apapa_ip):
        if apapa_ip:
            if DeviceInfo.objects.filter(main_ip=apapa_ip):
                instance = DeviceInfo.objects.filter(main_ip=apapa_ip)
                raise serializers.ValidationError("该ip和{}客户主ip冲突，请查看".format(instance[0].customer_token))
            if DeviceInfo.objects.filter(back_ip=apapa_ip):
                instance = DeviceInfo.objects.filter(back_ip=apapa_ip)
                raise serializers.ValidationError("该ip和{}客户副ip冲突，请查看".format(instance[0].customer_token))
            if DeviceInfo.objects.filter(~Q(customer_token=self.instance),apapa_ip=apapa_ip):
                instance = DeviceInfo.objects.filter(~Q(customer_token=self.instance),apapa_ip=apapa_ip)
                raise serializers.ValidationError("该ip和{}客户apapaip冲突，请查看".format(instance[0].customer_token))
            if DeviceInfo.objects.filter(cdn_ip=apapa_ip):
                instance = DeviceInfo.objects.filter(cdn_ip=apapa_ip)
                raise serializers.ValidationError("该ip和{}客户cdnip冲突，请查看".format(instance[0].customer_token))
            return apapa_ip
    def validate_cdn_ip(self,cdn_ip):
        if cdn_ip:
            if DeviceInfo.objects.filter(main_ip=cdn_ip):
                instance = DeviceInfo.objects.filter(main_ip=cdn_ip)
                raise serializers.ValidationError("该ip和{}客户主ip冲突，请查看".format(instance[0].customer_token))
            if DeviceInfo.objects.filter(back_ip=cdn_ip):
                instance = DeviceInfo.objects.filter(back_ip=cdn_ip)
                raise serializers.ValidationError("该ip和{}客户副ip冲突，请查看".format(instance[0].customer_token))
            if DeviceInfo.objects.filter(apapa_ip=cdn_ip):
                instance = DeviceInfo.objects.filter(apapa_ip=cdn_ip)
                raise serializers.ValidationError("该ip和{}客户apapaip冲突，请查看".format(instance[0].customer_token))
            if DeviceInfo.objects.filter(~Q(customer_token=self.instance),cdn_ip=cdn_ip):
                instance = DeviceInfo.objects.filter(~Q(customer_token=self.instance),cdn_ip=cdn_ip)
                raise serializers.ValidationError("该ip和{}客户cdnip冲突，请查看".format(instance[0].customer_token))
            return cdn_ip
    class Meta:
        model = DeviceInfo
        fields = "__all__"

class DeviceGroupListSerializer(serializers.ModelSerializer):
    group = DeviceCreateSerializer(many=True,help_text="主机")
    class Meta:
        model = DeviceGroup
        fields = ("id","group_name","groupdesc","group")