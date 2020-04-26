<template>
  <div style="margin-top: 15px;">
    <div class="filter-container">
      <el-form label-width="100px">
        <el-form-item label="IP地址">
          <el-input v-model="ipaddr" placeholder="请输入ip地址" style="width: 200px;" class="filter-item" />
          <el-button class="filter-item" type="primary" icon="el-icon-search" @click="ipSerch">
            搜索
          </el-button>
        </el-form-item>
      </el-form>
    </div>
    <el-card>
      <el-table
        :data="tableData"
        border
        style="width: 100%"
      >
        <el-table-column>
          <template slot-scope="props">
            <el-form label-position="left" inline class="demo-table-expand">
              <el-form-item label="IP地址">
                <span>{{ ipaddr }}</span>
              </el-form-item>
              <el-form-item label="国家">
                <span>{{ props.row.country_name }}</span>
              </el-form-item>
              <el-form-item label="城市">
                <span>{{ props.row.city || '无记录' }}</span>
              </el-form-item>
              <el-form-item label="国家代码">
                <span>{{ props.row.country_code }}</span>
              </el-form-item>
              <el-form-item label="大洲">
                <span>{{ props.row.country_code }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script>
import { getgeoip } from '@/api/geoip'

export default {
  data() {
    return {
      list: [{ id: 1, name: '深圳' }, { id: 2, name: '广州' }],
      ipaddr: '',
      // rules: {
      //   ipaddr: [
      //     { required: true, message: '请输入ip地址', trigger: 'blur' },
      //     { min: 7, max: 15, message: '请输入正确ip地址', trigger: 'blur' }
      //   ]
      // },
      listLoading: true,
      tableData: [
        {
          city: null,
          continent_code: null,
          continent_name: null,
          country_code: null,
          country_name: null,
          dma_code: null,
          latitude: null,
          longitude: null,
          postal_code: null,
          region: null,
          time_zone: null
        }
      ]
    }
  },
  created() {
    // this.fetchData()
  },
  methods: {
    getDataName(obj) {
      let name = obj.data
      if (Array.isArray(obj.dataList) && obj.dataList.length > 0) {
        for (let i = 0; i < obj.dataList.length; i++) {
          if (obj.dataList[i][obj.value] === obj.data) {
            name = obj.dataList[i][obj.label]
          }
        }
      }
      return name
    },
    ipSerch() {
      this.listLoading = true
      getgeoip({ ipaddress: this.ipaddr })
        .then(response => {
          this.tableData = [response]
          this.listLoading = false
          // this.$refs['ipaddrForm'].resetFields()
        })
        .catch(error => {
          console.log(error.response)
          const msg = error.response
          this.$message({
            type: 'warning',
            message: msg['ipaddr'][0],
            duration: 2 * 1000
          })
        })
    },
    onCancel() {
      this.$message({
        message: 'cancel!',
        type: 'warning'
      })
    }
  }
}
</script>

<style scoped>
.el-select .el-input {
  width: 130px;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
</style>
