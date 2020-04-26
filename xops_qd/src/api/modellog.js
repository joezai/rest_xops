import request from '@/utils/request'

export function LogSentryList() {
  return request({
    url: 'logs/logsentrys/',
    method: 'get'
  })
}
