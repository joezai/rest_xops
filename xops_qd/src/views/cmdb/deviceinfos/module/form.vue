<template>
  <el-dialog :append-to-body="true" :visible.sync="dialog" :title="isAdd ? '新增资产' : '编辑资产'" width="600px">
    <el-form ref="form" :model="form" size="small" label-width="80px">
      <el-form-item label="客户名称" prop="name">
        <el-input v-model="form.customer" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="客户编码" prop="name">
        <el-input v-model="form.customer_token" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="主记录" prop="name">
        <el-input v-model="form.main_record" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="副记录" prop="name">
        <el-input v-model="form.sub_record" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="cdn记录" prop="name">
        <el-input v-model="form.cdn_record" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="主ip" prop="name">
        <el-input v-model="form.main_ip" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="副ip" prop="name">
        <el-input v-model="form.back_ip" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="APAPAip" prop="name">
        <el-input v-model="form.apapa_ip" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="CDNip" prop="name">
        <el-input v-model="form.cdn_ip" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="LANip" prop="name">
        <el-input v-model="form.lan_ip" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="创立者" prop="name">
        <el-input v-model="form.creater" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="主机类型" prop="name">
        <el-input v-model="form.device_type" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="主机IDC" prop="name">
        <el-input v-model="form.idc_location" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="上线状态" prop="name">
        <el-input v-model="form.online_state" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="测试API" prop="name">
        <el-input v-model="form.testapi_state" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="设备描述" prop="name">
        <el-input v-model="form.device_desc" placeholder="" style="width: 460px;"/>
      </el-form-item>
      <el-form-item label="设备分组" prop="name">
        <el-input v-model="form.device_group" placeholder="" style="width: 460px;"/>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button type="text" @click="cancel">取消</el-button>
      <el-button :loading="loading" type="primary" @click="doSubmit">确认</el-button>
    </div>
  </el-dialog>
</template>

<script>
import { add, edit } from '@/api/deviceinfos'
import Treeselect from '@riophae/vue-treeselect'
import IconSelect from '@/components/IconSelect'
import '@riophae/vue-treeselect/dist/vue-treeselect.css'
export default {
  components: { Treeselect, IconSelect },
  props: {
    deviceinfos: {
      type: Array,
      required: true
    },
    isAdd: {
      type: Boolean,
      required: true
    },
    sup_this: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      loading: false, dialog: false,
      form: { id: '', customer: '', customer_token: '', main_record: '', sub_record: '', cdn_record: '', main_ip: '', back_ip: '', apapa_ip: '', cdn_ip: '', creater: '', device_type: '主站', lan_ip: '', idc_location: '', online_state: '', testapi_state: '', device_desc: '', device_group: '' }
    }
  },
  methods: {
    cancel() {
      this.resetForm()
    },
    doSubmit() {
      this.$refs['form'].validate((valid) => {
        if (valid) {
          this.loading = true
          if (this.isAdd) {
            this.doAdd()
          } else this.doEdit()
        } else {
          return false
        }
      })
    },
    doAdd() {
      add(this.form).then(res => {
        this.resetForm()
        this.$message({
          showClose: true,
          type: 'success',
          message: '添加成功!',
          duration: 2500
        })
        this.loading = false
        this.$parent.$parent.init()
        this.$parent.$parent.getDeviceinfos()
      }).catch(err => {
        this.loading = false
        console.log(err)
      })
    },
    doEdit() {
      edit(this.form.id, this.form).then(res => {
        this.resetForm()
        this.$message({
          showClose: true,
          type: 'success',
          message: '修改成功!',
          duration: 2500
        })
        this.loading = false
        this.sup_this.init()
        this.sup_this.getDeviceinfos()
      }).catch(err => {
        this.loading = false
        console.log(err)
      })
    },
    resetForm() {
      this.dialog = false
      this.$refs['form'].resetFields()
      this.form = { id: '', customer: '', customer_token: '', main_record: '', sub_record: '', cdn_record: '', main_ip: '', back_ip: '', apapa_ip: '', cdn_ip: '', creater: '', device_type: '主站', lan_ip: '', idc_location: '', online_state: '', testapi_state: '', device_desc: '', device_group: '' }
    },
    selected(name) {
      this.form.icon = name
    }
  }
}
</script>

<style scoped>

</style>
