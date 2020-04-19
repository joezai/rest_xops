<template>
  <div class="app-container">
    <eHeader :deviceinfos="deviceinfos" :query="query"/>
    <!--表格渲染-->
    <tree-table v-loading="loading" :data="data" :expand-all="true" :columns="columns" border size="small">
      <el-table-column label="操作" width="150px" align="center">
        <template slot-scope="scope">
          <edit v-if="checkPermission(['admin','menu_all','menu_edit'])" :deviceinfos="deviceinfos" :data="scope.row" :sup_this="sup_this"/>
          <el-popover
            v-if="checkPermission(['admin','menu_all','menu_delete'])"
            :ref="scope.row.id"
            placement="top"
            width="200">
            <p>确定删除吗,如果存在下级节点则节点上升，此操作不能撤销！</p>
            <div style="text-align: right; margin: 0">
              <el-button size="mini" type="text" @click="$refs[scope.row.id].doClose()">取消</el-button>
              <el-button :loading="delLoading" type="primary" size="mini" @click="subDelete(scope.row.id)">确定</el-button>
            </div>
            <el-button slot="reference" :disabled="scope.row.id === 1" type="danger" size="mini">删除</el-button>
          </el-popover>
        </template>
      </el-table-column>
    </tree-table>
    <el-pagination
      :total="total"
      :page-sizes="[100, 200, 300, 400]"
      style="margin-top: 8px;"
      layout="total, prev, pager, next, sizes"
      @size-change="sizeChange"
      @current-change="pageChange"/>
  </div>
</template>

<script>
import checkPermission from '@/utils/permission' // 权限判断函数
import treeTable from '@/components/TreeTable'
import initData from '@/mixins/initData'
import { del, getdeviceinfos } from '@/api/deviceinfos'
import { parseTime } from '@/utils/index'
import eHeader from './module/header'
import edit from './module/edit'
export default {
  components: { eHeader, edit, treeTable },
  mixins: [initData],
  data() {
    return {
      columns: [
        {
          text: '服务器类型',
          value: 'device_type'
        },
        {
          text: '客户名称',
          value: 'customer'
        },
        {
          text: '客户编码',
          value: 'customer_token'
        },
        {
          text: '主ip',
          value: 'main_ip'
        },
        {
          text: '副ip',
          value: 'back_ip'
        },
        {
          text: 'APAPAip',
          value: 'apapa_ip'
        },
        {
          text: 'CDNip',
          value: 'cdn_ip'
        },
        {
          text: '上线状态',
          value: 'online_state'
        }
      ],
      delLoading: false, sup_this: this, deviceinfos: []
    }
  },
  created() {
    this.getDeviceinfos()
    this.$nextTick(() => {
      this.init(
        this.size = 100
      )
    })
  },
  methods: {
    parseTime,
    checkPermission,
    beforeInit() {
      this.url = 'api/cmdb/deviceinfos/'
      const sort = 'sort'
      const query = this.query
      const value = query.value
      this.params = { page: this.page, size: this.size, ordering: sort }
      if (value) { this.params['search'] = value }
      return true
    },
    subDelete(id) {
      this.delLoading = true
      del(id).then(res => {
        this.delLoading = false
        this.$refs[id].doClose()
        this.init()
        this.$message({
          showClose: true,
          type: 'success',
          message: '删除成功!',
          duration: 2500
        })
      }).catch(err => {
        this.delLoading = false
        this.$refs[id].doClose()
        console.log(err)
      })
    },
    getDeviceinfos() {
      getdeviceinfos().then(res => {
        this.deviceinfos = res.results
      })
    }
  }
}
</script>

<style scoped>

</style>
