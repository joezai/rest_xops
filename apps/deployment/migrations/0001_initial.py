# Generated by Django 2.1.7 on 2020-03-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeployRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(default='', max_length=100, verbose_name='部署名称')),
                ('record_id', models.CharField(default='', max_length=100, verbose_name='本次记录')),
                ('alias', models.CharField(default='', max_length=100, verbose_name='别名')),
                ('status', models.CharField(blank=True, max_length=20, null=True, verbose_name='状态')),
                ('project_id', models.IntegerField(blank=True, null=True, verbose_name='关联项目')),
                ('server_ids', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='关联主机')),
                ('target_root', models.CharField(default='', max_length=200, verbose_name='部署路径')),
                ('target_releases', models.CharField(default='', max_length=200, verbose_name='目标仓库')),
                ('prev_record', models.CharField(default='', max_length=100, verbose_name='前次记录')),
                ('is_rollback', models.BooleanField(default=False, verbose_name='可否回滚')),
            ],
            options={
                'verbose_name': '部署记录',
                'verbose_name_plural': '部署记录',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(default='', max_length=100, verbose_name='项目名称')),
                ('alias', models.CharField(default='', max_length=100, verbose_name='别名')),
                ('environment', models.CharField(default='', max_length=30, verbose_name='环境')),
                ('status', models.CharField(blank=True, max_length=20, null=True, verbose_name='状态')),
                ('excludes', models.TextField(blank=True, null=True, verbose_name='排除')),
                ('is_include', models.BooleanField(default=False, verbose_name='包含')),
                ('is_link', models.BooleanField(default=True, verbose_name='是否link')),
                ('target_root', models.CharField(default='', max_length=200, verbose_name='部署路径')),
                ('target_releases', models.CharField(default='', max_length=200, verbose_name='目标仓库')),
                ('task_envs', models.TextField(blank=True, null=True, verbose_name='全局变量')),
                ('prev_deploy', models.TextField(blank=True, null=True, verbose_name='deploy前置')),
                ('post_deploy', models.TextField(blank=True, null=True, verbose_name='deploy后置')),
                ('prev_release', models.TextField(blank=True, null=True, verbose_name='release前置')),
                ('post_release', models.TextField(blank=True, null=True, verbose_name='release后置')),
                ('version_num', models.IntegerField(blank=True, null=True, verbose_name='版本数量')),
                ('repo_url', models.CharField(default='', max_length=200)),
                ('repo_mode', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('server_ids', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='关联主机')),
                ('last_task_status', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='状态')),
                ('app_start', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='启动脚本')),
                ('app_stop', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='停止脚本')),
                ('app_log_path', models.CharField(blank=True, default='', max_length=150, null=True, verbose_name='日志目录')),
                ('app_log_file', models.CharField(blank=True, default='', max_length=150, null=True, verbose_name='日志文件')),
                ('user_id', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='关联用户id')),
            ],
            options={
                'verbose_name': '项目配置',
                'verbose_name_plural': '项目配置',
            },
        ),
    ]
