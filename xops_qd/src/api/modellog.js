import request from '@/utils/request'

export function LogSentryList(data) {
  return request({
    url: '/logs/logsentrys/',
    method: 'get',
    params: data
  })
}
export function LogSentryDetail(id) {
  return request({
    url: '/logs/logsentrys/' + id,
    method: 'get'
  })
}
