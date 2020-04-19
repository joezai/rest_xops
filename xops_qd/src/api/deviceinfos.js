import request from '@/utils/request'

// 获取所有的分组
export function getdeviceinfos() {
  return request({
    url: 'api/cmdb/deviceinfos/',
    method: 'get'
  })
}

export function add(data) {
  return request({
    url: 'api/cmdb/deviceinfos/',
    method: 'post',
    data
  })
}

export function del(id) {
  return request({
    url: 'api/cmdb/deviceinfos/' + id + '/',
    method: 'delete'
  })
}

export function edit(id, data) {
  return request({
    url: 'api/cmdb/deviceinfos/' + id + '/',
    method: 'put',
    data
  })
}

export function retrieve(id) {
  return request({
    url: 'api/cmdb/deviceinfos/' + id + '/',
    method: 'get'
  })
}

export function save(id, data) {
  return request({
    url: 'api/cmdb/deviceinfos/' + id + '/',
    method: 'patch',
    data
  })
}
