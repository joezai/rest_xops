import request from '@/utils/request'

export function add(data) {
  return request({
    url: 'api/rbac/users/',
    method: 'post',
    data
  })
}

export function del(id) {
  return request({
    url: 'api/rbac/users/' + id + '/',
    method: 'delete'
  })
}

export function edit(id, data) {
  return request({
    url: 'api/rbac/users/' + id + '/',
    method: 'put',
    data
  })
}

export function updatePasswd(id, data) {
  return request({
    url: 'api/rbac/users/' + id + '/change-passwd/',
    method: 'post',
    data
  })
}

export function getUserList(name) {
  if (name) {
    return request({
      url: 'api/rbac/user/list/?name=' + name,
      method: 'get'
    })
  } else {
    return request({
      url: 'api/rbac/user/list/',
      method: 'get'
    })
  }
}

