import request from '@/utils/request'

export function LogSentryList() {
  return request({
    url: 'logs/logsentrys/',
    method: 'get'
  })
}
export function LogSentryDetail(id) {
  return request({
    url: '/logs/logsentrys/' + id,
    method: 'get'
  })
}
