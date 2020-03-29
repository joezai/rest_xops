import request from '@/utils/request'

export function login(username, password) {
  return request({
    url: 'api/rbac/auth/login/',
    method: 'post',
    data: {
      username,
      password
    }
  })
}

export function getInfo() {
  return request({
    url: 'api/rbac/auth/info/',
    method: 'get'
  })
}

export function buildMenus() {
  return request({
    url: 'api/rbac/auth/build/menus/',
    method: 'get'
  })
}
