# Generated by Django 2.1.7 on 2020-04-15 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('group_name', models.CharField(help_text='分组名称', max_length=100, verbose_name='分组名称')),
                ('groupdesc', models.CharField(help_text='分组描述', max_length=200, verbose_name='分组描述')),
                ('change_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '资产分组',
                'verbose_name_plural': '资产分组',
            },
        ),
        migrations.CreateModel(
            name='DeviceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('device_type', models.CharField(choices=[('zz', '主站'), ('bz', '备站'), ('zk', '主库'), ('ck', '从库'), ('zzzk', '主站主库'), ('bzck', '备份从库')], default='zz', help_text='资产类型: 1(主站),2(备站),3(主库),4(从库),5(主站主库),6(备份从库)', max_length=10, verbose_name='资产类型')),
                ('customer', models.CharField(help_text='客户', max_length=100, verbose_name='客户')),
                ('customer_token', models.CharField(help_text='商户编码', max_length=30, verbose_name='商户编码')),
                ('main_record', models.CharField(help_text='主解析记录', max_length=100, verbose_name='主解析记录')),
                ('sub_record', models.CharField(help_text='副解析记录', max_length=100, verbose_name='副解析记录')),
                ('cdn_record', models.CharField(help_text='cdn解析记录', max_length=100, verbose_name='cdn解析记录')),
                ('main_ip', models.GenericIPAddressField(help_text='主ip', verbose_name='主ip')),
                ('back_ip', models.GenericIPAddressField(help_text='副ip', verbose_name='副ip')),
                ('apapa_ip', models.GenericIPAddressField(help_text='APAPAip', null=True, verbose_name='APAPAip')),
                ('cdn_ip', models.GenericIPAddressField(help_text='CDNip', null=True, verbose_name='CDNip')),
                ('lan_ip', models.GenericIPAddressField(help_text='内网ip', null=True, verbose_name='内网ip')),
                ('idc_location', models.CharField(choices=[('GD', '广东'), ('WH', '武汉'), ('SH', '上海')], default='GD', help_text='服务器位置: 1(广东),2(武汉),3(上海)', max_length=10, verbose_name='服务器位置')),
                ('online_state', models.CharField(choices=[('wsx', '未上线'), ('ysx', '已上线'), ('dqy', '待迁移'), ('dhs', '待回收')], default='wsx', help_text='上线状态: 1(未上线),2(已上线),3(待迁移),4(待回收)', max_length=10, verbose_name='上线状态')),
                ('testapi_state', models.CharField(choices=[('wkt', '未开通'), ('ykt', '已开通')], default='wkt', help_text='测试api开通状态: 1(未开通),2(已开通)', max_length=10, verbose_name='测试api开通状态')),
                ('creater', models.CharField(help_text='搭建人', max_length=30, verbose_name='搭建人')),
                ('device_desc', models.TextField(blank=True, default='', help_text='资产备注', verbose_name='资产备注')),
                ('changed_by', models.ForeignKey(blank=True, help_text='修改人', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('device_group', models.ForeignKey(help_text='资产分组', on_delete=django.db.models.deletion.CASCADE, related_name='group', to='cmdb.DeviceGroup', verbose_name='资产分组')),
            ],
            options={
                'verbose_name': '设备信息',
                'verbose_name_plural': '设备信息',
            },
        ),
        migrations.CreateModel(
            name='HistoricalDeviceGroup',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('group_name', models.CharField(help_text='分组名称', max_length=100, verbose_name='分组名称')),
                ('groupdesc', models.CharField(help_text='分组描述', max_length=200, verbose_name='分组描述')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('change_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical 资产分组',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDeviceInfo',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('device_type', models.CharField(choices=[('zz', '主站'), ('bz', '备站'), ('zk', '主库'), ('ck', '从库'), ('zzzk', '主站主库'), ('bzck', '备份从库')], default='zz', help_text='资产类型: 1(主站),2(备站),3(主库),4(从库),5(主站主库),6(备份从库)', max_length=10, verbose_name='资产类型')),
                ('customer', models.CharField(help_text='客户', max_length=100, verbose_name='客户')),
                ('customer_token', models.CharField(help_text='商户编码', max_length=30, verbose_name='商户编码')),
                ('main_record', models.CharField(help_text='主解析记录', max_length=100, verbose_name='主解析记录')),
                ('sub_record', models.CharField(help_text='副解析记录', max_length=100, verbose_name='副解析记录')),
                ('cdn_record', models.CharField(help_text='cdn解析记录', max_length=100, verbose_name='cdn解析记录')),
                ('main_ip', models.GenericIPAddressField(help_text='主ip', verbose_name='主ip')),
                ('back_ip', models.GenericIPAddressField(help_text='副ip', verbose_name='副ip')),
                ('apapa_ip', models.GenericIPAddressField(help_text='APAPAip', null=True, verbose_name='APAPAip')),
                ('cdn_ip', models.GenericIPAddressField(help_text='CDNip', null=True, verbose_name='CDNip')),
                ('lan_ip', models.GenericIPAddressField(help_text='内网ip', null=True, verbose_name='内网ip')),
                ('idc_location', models.CharField(choices=[('GD', '广东'), ('WH', '武汉'), ('SH', '上海')], default='GD', help_text='服务器位置: 1(广东),2(武汉),3(上海)', max_length=10, verbose_name='服务器位置')),
                ('online_state', models.CharField(choices=[('wsx', '未上线'), ('ysx', '已上线'), ('dqy', '待迁移'), ('dhs', '待回收')], default='wsx', help_text='上线状态: 1(未上线),2(已上线),3(待迁移),4(待回收)', max_length=10, verbose_name='上线状态')),
                ('testapi_state', models.CharField(choices=[('wkt', '未开通'), ('ykt', '已开通')], default='wkt', help_text='测试api开通状态: 1(未开通),2(已开通)', max_length=10, verbose_name='测试api开通状态')),
                ('creater', models.CharField(help_text='搭建人', max_length=30, verbose_name='搭建人')),
                ('device_desc', models.TextField(blank=True, default='', help_text='资产备注', verbose_name='资产备注')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('changed_by', models.ForeignKey(blank=True, db_constraint=False, help_text='修改人', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('device_group', models.ForeignKey(blank=True, db_constraint=False, help_text='资产分组', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='cmdb.DeviceGroup', verbose_name='资产分组')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical 设备信息',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
