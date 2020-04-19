import request from '@/utils/request'

// 获取所有的分组
export function getdevicegroups() {
  return request({
    url: 'api/cmdb/devicegroups/',
    method: 'get'
  })
}

export function add(data) {
  return request({
    url: 'api/cmdb/devicegroups/',
    method: 'post',
    data
  })
}

export function del(id) {
  return request({
    url: 'api/cmdb/devicegroups/' + id + '/',
    method: 'delete'
  })
}

export function edit(id, data) {
  return request({
    url: 'api/cmdb/devicegroups/' + id + '/',
    method: 'put',
    data
  })
}

export function retrieve(id) {
  return request({
    url: 'api/cmdb/devicegroups/' + id + '/',
    method: 'get'
  })
}

export function save(id, data) {
  return request({
    url: 'api/cmdb/devicegroups/' + id + '/',
    method: 'patch',
    data
  })
}
