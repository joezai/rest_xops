import request from '@/utils/request'

// 获取所有的权限树
export function getPermissionTree() {
  return request({
    url: 'api/rbac/permission/tree/',
    method: 'get'
  })
}

export function add(data) {
  return request({
    url: 'api/rbac/permissions/',
    method: 'post',
    data
  })
}

export function del(id) {
  return request({
    url: 'api/rbac/permissions/' + id + '/',
    method: 'delete'
  })
}

export function edit(id, data) {
  return request({
    url: 'api/rbac/permissions/' + id + '/',
    method: 'put',
    data
  })
}

export function retrieve(id) {
  return request({
    url: 'api/rbac/permissions/' + id + '/',
    method: 'get'
  })
}

export function save(id, data) {
  return request({
    url: 'api/rbac/permissions/' + id + '/',
    method: 'patch',
    data
  })
}
