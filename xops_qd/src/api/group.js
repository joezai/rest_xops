import request from '@/utils/request'

export function getGroups() {
  return request({
    url: 'api/cmdb/groups/',
    method: 'get'
  })
}

export function add(data) {
  return request({
    url: 'api/cmdb/groups/',
    method: 'post',
    data
  })
}

export function del(id) {
  return request({
    url: 'api/cmdb/groups/' + id + '/',
    method: 'delete'
  })
}

export function retrieve(id) {
  return request({
    url: 'api/cmdb/groups/' + id + '/',
    method: 'get'
  })
}

export function edit(id, data) {
  return request({
    url: 'api/cmdb/groups/' + id + '/',
    method: 'put',
    data
  })
}

export function save(id, data) {
  return request({
    url: 'api/cmdb/groups/' + id + '/',
    method: 'patch',
    data
  })
}

