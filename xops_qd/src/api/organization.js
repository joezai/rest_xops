import request from '@/utils/request'

// 获取所有的organization
export function getOrganizationTree() {
  return request({
    url: 'api/rbac/organization/tree/',
    method: 'get'
  })
}

// 获取所有的user
export function getOrganizationUserTree() {
  return request({
    url: 'api/rbac/organization/user/tree/',
    method: 'get'
  })
}

export function add(data) {
  return request({
    url: 'api/rbac/organizations/',
    method: 'post',
    data
  })
}

export function del(id) {
  return request({
    url: 'api/rbac/organizations/' + id + '/',
    method: 'delete'
  })
}

export function edit(id, data) {
  return request({
    url: 'api/rbac/organizations/' + id + '/',
    method: 'put',
    data
  })
}
