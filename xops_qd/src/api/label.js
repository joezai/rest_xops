import request from '@/utils/request'

export function getLabels() {
  return request({
    url: 'api/cmdb/labels/',
    method: 'get'
  })
}

export function add(data) {
  return request({
    url: 'api/cmdb/labels/',
    method: 'post',
    data
  })
}

export function del(id) {
  return request({
    url: 'api/cmdb/labels/' + id + '/',
    method: 'delete'
  })
}

export function retrieve(id) {
  return request({
    url: 'api/cmdb/labels/' + id + '/',
    method: 'get'
  })
}

export function edit(id, data) {
  return request({
    url: 'api/cmdb/labels/' + id + '/',
    method: 'put',
    data
  })
}

export function save(id, data) {
  return request({
    url: 'api/cmdb/labels/' + id + '/',
    method: 'patch',
    data
  })
}

