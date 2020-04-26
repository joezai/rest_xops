import request from '@/utils/request'

export function getgeoip(data) {
  return request({
    url: 'api/cmdb/geoipcheck/?ipaddress=' + data.ipaddress,
    method: 'get'
  })
}
