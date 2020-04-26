export const methodOptions = [
  { key: 'ALL', display_name: 'ALL' },
  { key: 'GET', display_name: 'GET' },
  { key: 'POST', display_name: 'POST' },
  { key: 'PUT', display_name: 'PUT' },
  { key: 'PATCH', display_name: 'PATCH' },
  { key: 'DELETE', display_name: 'DELETE' }
]
export const userTypeOptions = [
  { key: 'customuser', display_name: '自定义用户' },
  { key: 'anonymous', display_name: '匿名用户' },
  { key: 'authenticated', display_name: '已认证用户' }
]

export const isActiveOptions = [
  { key: true, display_name: '是' },
  { key: false, display_name: '否' }
]

export const MountOptions = [
  { key: 0, display_name: '未挂载' },
  { key: 1, display_name: '已挂载' }
]

export const ActionOptions = [
  { key: 1, display_name: '添加' },
  { key: 2, display_name: '修改' },
  { key: 3, display_name: '删除' }
]

export const assetOptions = [
  { key: '生产主机', value: 'prod' },
  { key: '中心主机', value: 'center' },
  { key: '手机主机', value: 'mobile' },
  { key: '棋牌主机', value: 'chess' },
  { key: '监控主机', value: 'monitor' },
  { key: '采集主机', value: 'collect' },
  { key: 'CDN节点', value: 'cdn' },
  { key: '全部', value: '' }
]

export const statusOptions = [
  { key: '未上线', value: 0 },
  { key: '已上线', value: 1 },
  { key: '全部', value: '' }
]
export const hostTypeOptions = [
  { key: '主站主库', value: 'zzzk' },
  { key: '备份从库', value: 'bfck' },
  { key: '主站', value: 'zz' },
  { key: '备份', value: 'bf' },
  { key: '主库', value: 'zk' },
  { key: '从库', value: 'ck' }
]
