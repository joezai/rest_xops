# @Time    : 2019/2/27 14:42
# @Author  : xufqing
from django.urls import include
from deployment.views import project, deploy, applog
from rest_framework import routers
from django.conf.urls import url
router = routers.DefaultRouter()
router.register(r'projects', project.ProjectViewSet, base_name="projects")
router.register(r'deploy/records', deploy.DeployRecordViewSet, base_name="deploy_record")
app_name = 'deploymnet'
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'deploy/excu/', deploy.DeployView.as_view(), name='deploy'),
    url(r'deploy/ver/', deploy.VersionView.as_view(), name='version'),
    url(r'deploy/applog/', applog.AppLogView.as_view(), name='applog'),
    url(r'project/copy/', project.ProjectCopy.as_view(), name='project_copy')
]