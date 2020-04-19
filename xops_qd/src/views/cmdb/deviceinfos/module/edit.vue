<template>
  <div>
    <el-button :disabled="data.id === 1" size="mini" type="success" @click="to">编辑</el-button>
    <eForm ref="form" :deviceinfos="deviceinfos" :sup_this="sup_this" :is-add="false"/>
  </div>
</template>
<script>
import eForm from './form'
export default {
  components: { eForm },
  props: {
    data: {
      type: Object,
      required: true
    },
    sup_this: {
      type: Object,
      required: true
    },
    deviceinfos: {
      type: Array,
      required: true
    }
  },
  methods: {
    to() {
      const _this = this.$refs.form
      _this.form = {
        id: this.data.id,
        customer: this.data.customer,
        customer_token: this.data.customer_token,
        main_record: this.data.main_record,
        sub_record: this.data.sub_record,
        cdn_record: this.data.cdn_record,
        main_ip: this.data.main_ip,
        back_ip: this.data.back_ip,
        apapa_ip: this.data.apapa_ip,
        cdn_ip: this.data.cdn_ip,
        creater: this.data.creater,
        device_type: this.data.device_type,
        lan_ip: this.data.lan_ip,
        idc_location: this.data.idc_location,
        online_state: this.data.online_state,
        testapi_state: this.data.testapi_state,
        device_desc: this.data.device_desc,
        device_group: this.data.device_group
      }
      _this.dialog = true
    }
  }
}
</script>

<style scoped>
  div{
    display: inline-block;
    margin-right: 3px;
  }
</style>
