from django.urls import include
from rbac.views import user,organization,menu,role,permission
from rest_framework import routers
from django.conf.urls import url
router = routers.DefaultRouter()
router.register(r'users', user.UserViewSet, basename="users")
router.register(r'organizations', organization.OrganizationViewSet, basename="organization")
router.register(r'menus', menu.MenuViewSet, basename="menus")
router.register(r'permissions', permission.PermissionViewSet, basename="permissions")
router.register(r'roles', role.RoleViewSet, basename="roles")
router.register(r'avatars', user.UserAvatarView, basename="avatars")
app_name = 'rbac'

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'auth/login/', user.UserAuthView.as_view()),
    url(r'auth/info/', user.UserInfoView.as_view(), name='user_info'),
    url(r'auth/build/menus/', user.UserBuildMenuView.as_view(), name='build_menus'),
    url(r'organization/tree/', organization.OrganizationTreeView.as_view(),name='organizations_tree'),
    url(r'organization/user/tree/', organization.OrganizationUserTreeView.as_view(), name='organization_user_tree'),
    url(r'menu/tree/', menu.MenuTreeView.as_view(), name='menus_tree'),
    url(r'permission/tree/', permission.PermissionTreeView.as_view(), name='permissions_tree'),
    url(r'user/list/', user.UserListView.as_view(), name='user_list'),
]
