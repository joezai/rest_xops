from django.db import models
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords
from datetime import datetime

User = get_user_model()

class TimeAbstract(models.Model):
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    class Meta:
        abstract = True

class DeviceGroup(TimeAbstract):
    '''
    资产分组
    '''
    group_name = models.CharField(max_length=100,verbose_name='分组名称',help_text="分组名称")
    groupdesc = models.CharField(max_length=200,verbose_name="分组描述",help_text="分组描述")
    change_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    history = HistoricalRecords(excluded_fields=['add_time', 'modify_time'])
    class Meta:
        verbose_name = "资产分组"
        verbose_name_plural = verbose_name
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    def __str__(self):
        return self.group_name

class DeviceInfo(TimeAbstract):
    '''
    资产信息表
    '''
    device_type_choice = (
        ('主站', "主站"),
        ('备站', "备站"),
        ('主库', "主库"),
        ('从库', "从库"),
        ('主站主库', "主站主库"),
        ('备站从库', "备份从库")
    )
    idc_location_choice = (
        ("广东", "广东"),
        ("武汉", "武汉"),
        ("上海", "上海")
    )
    online_state_choice = (
        ("未上线", "未上线"),
        ("已上线", "已上线"),
        ("待迁移", "待迁移"),
        ("待回收", "待回收")
    )
    testapi_state_choice= (
        ("未开通", "未开通"),
        ("已开通", "已开通")
    )
    device_type = models.CharField(default='主站', choices=device_type_choice, max_length=100, verbose_name="资产类型",
                                      help_text=u"资产类型: 1(主站),2(备站),3(主库),4(从库),5(主站主库),6(备份从库)")
    customer = models.CharField(max_length=100,verbose_name='客户',help_text="客户")
    customer_token = models.CharField(max_length=30,verbose_name='商户编码',help_text="商户编码")
    main_record = models.CharField(max_length=100,verbose_name='主解析记录',help_text="主解析记录")
    sub_record = models.CharField(max_length=100,verbose_name='副解析记录',help_text="副解析记录")
    cdn_record = models.CharField(max_length=100,verbose_name='cdn解析记录',help_text="cdn解析记录")
    main_ip = models.GenericIPAddressField(null=False,blank=False,verbose_name='主ip',help_text="主ip")
    back_ip = models.GenericIPAddressField(null=False,blank=False,verbose_name='副ip',help_text="副ip")
    apapa_ip = models.GenericIPAddressField(null=True,verbose_name='APAPAip',help_text="APAPAip")
    cdn_ip = models.GenericIPAddressField(null=True,verbose_name='CDNip',help_text="CDNip")
    lan_ip = models.GenericIPAddressField(null=True,verbose_name='内网ip',help_text="内网ip")
    idc_location = models.CharField(default="广东", choices=idc_location_choice, max_length=10, verbose_name="服务器位置",
                                      help_text=u"服务器位置: 1(广东),2(武汉),3(上海)")
    online_state = models.CharField(default="未上线", choices=online_state_choice, max_length=10, verbose_name="上线状态",
                                       help_text=u"上线状态: 1(未上线),2(已上线),3(待迁移),4(待回收)")
    testapi_state = models.CharField(default="未开通", choices=testapi_state_choice, max_length=10, verbose_name="测试api开通状态",
                                        help_text=u"测试api开通状态: 1(未开通),2(已开通)")
    creater = models.CharField(max_length=30,verbose_name='搭建人',help_text="搭建人")
    device_group = models.ForeignKey(DeviceGroup,on_delete=models.CASCADE,verbose_name='资产分组',related_name="group",help_text="资产分组")
    device_desc = models.TextField(blank=True, default='', verbose_name='资产备注',help_text="资产备注")
    changed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL,help_text="修改人")
    history = HistoricalRecords(excluded_fields=['add_time', 'modify_time'])

    class Meta:
        verbose_name = '设备信息'
        verbose_name_plural = verbose_name

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    def __str__(self):
        return self.customer_token
