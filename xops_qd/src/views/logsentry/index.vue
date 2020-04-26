<template>
  <div class="app-container">
    <div class="filter-container">
      <el-select v-model="listQuery.action_flag" :placeholder="'操作类型'" clearable class="filter-item" style="width: 10%!important;" filterable @change="handleFilter">
        <el-option v-for="item in ActionOptions" :key="item.key" :label="item.display_name" :value="item.key" />
      </el-select>

      <el-input v-model="listQuery.search" style="width: 200px;" class="filter-item" clearable @keyup.enter.native="handleFilter" />
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">搜索</el-button>
    </div>

    <el-table
      v-loading="listLoading"
      :key="tableKey"
      :data="list"
      border
      style="width: 100%"
      height="700"
      stripe
      tooltip-effect="dark"
    >
      <el-table-column label="ID" prop="id" sortable="custom" align="center" width="65">
        <template slot-scope="scope">
          <span>{{ scope.row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column :formatter="dateFormat" label="操作时间" prop="time_added" width="180" />
      <el-table-column label="用户" width="120">
        <template slot-scope="scope">
          <span>{{ scope.row.user }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作类型" width="100">
        <template slot-scope="scope">
          <span>{{ scope.row.action }}</span>
        </template>
      </el-table-column>
      <el-table-column label="数据库表名" width="100">
        <template slot-scope="scope">
          <span>{{ scope.row.content_type }}</span>
        </template>
      </el-table-column>
      <el-table-column label="日志记录">
        <template slot-scope="scope">
          <span>{{ scope.row.message }}</span>
        </template>
      </el-table-column>
    </el-table>

    <el-pagination
      :total="total"
      :current-page="page"
      :page-sizes="[10, 20, 50, 100]"
      :page-size="pagesize"
      style="float:right"
      layout="total, sizes, prev, pager, next, jumper"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />
  </div>
</template>

<script>
import { LogSentryList } from '@/api/modellog'
import { ActionOptions } from '@/utils/dict'
import moment from 'moment'

export default {
  name: 'ModellogLogsentry',

  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      pagesize: 10,
      page: 1,
      listLoading: false,
      listQuery: {
        page: 1,
        ordering: '-id',
        search: '',
        action_flag: '',
        content_type: ''
      },
      ActionOptions
    }
  },
  created() {
    this.getList()
    // this.getModelList()
  },
  methods: {
    dateFormat(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    },
    getList() {
      this.listLoading = true
      this.listQuery.pagesize = this.pagesize
      this.listQuery.page = this.page
      LogSentryList(this.listQuery).then(response => {
        this.list = response.results
        this.total = response.count
        this.listLoading = false
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.listQuery.pagesize = ''
      this.getList()
    },
    handleSizeChange(val) {
      this.pagesize = val
      this.getList()
    },
    handleCurrentChange(val) {
      this.page = val
      this.getList()
    }

  }
}
</script>
