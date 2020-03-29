import request from '@/utils/request'

export function add(data) {
  return request({
    url: 'api/deployment/projects/',
    method: 'post',
    data
  })
}

export function retrieve(id) {
  return request({
    url: 'api/deployment/projects/' + id + '/',
    method: 'get'
  })
}

export function del(id) {
  return request({
    url: 'api/deployment/projects/' + id + '/',
    method: 'delete'
  })
}

export function edit(id, data) {
  return request({
    url: 'api/deployment/projects/' + id + '/',
    method: 'put',
    data
  })
}

export function copy(data) {
  return request({
    url: 'api/deployment/project/copy/',
    method: 'post',
    data
  })
}
