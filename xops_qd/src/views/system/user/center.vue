<template>
  <div class="app-container">
    <div id="content-main" style="width:600px;">
      <el-card shadow="never" class="box-card user-info">
        <div class="avatar-content">
          <el-upload
            :show-file-list="false"
            :http-request="upLoad"
            :on-success="handleSuccess"
            :on-error="handleError"
            :headers="headers"
            action=""
            class="avatar-uploader">
            <img v-if="avatar" :src="avatar" title="点击上传头像" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"/>
          </el-upload>
        </div>
        <div class="user-info-content">
          <div>登录账号：{{ name }}</div>
          <div>注册时间：{{ createTime }}</div>
          <div>账号状态：<span style="color: #909399">正常</span></div>
        </div>
      </el-card>
      <el-card shadow="never" class="box-card reset-pass">
        <h4 class="account-label-icon">登录密码：</h4>
        <updatePass :id="id"/>
        <p>安全性高的密码可使账号更安全，建议设置同时包含字母，数字，符号的密码。</p>
      </el-card>

      <!-- <el-card shadow="never" class="box-card reset-email">
        <h4 class="account-label-icon">邮箱验证：</h4>
        <updateEmail :email="email"/>
        <p>你的邮箱：{{ formatEmail(email) }} </p>
        <h4>绑定邮箱可用于</h4>
        <ul>
          <li>安全管理，密码重置与修改</li>
          <li>账号使用，使用邮箱登录系统</li>
        </ul>
      </el-card> -->
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import updatePass from './center/updatePass'
import { getToken } from '@/utils/auth'
import store from '@/store'
import axios from 'axios'
export default {
  name: 'Center',
  components: { updatePass },
  data() {
    return {
      headers: {
        'Authorization': 'Bearer ' + getToken()
      }
    }
  },
  computed: {
    ...mapGetters([
      'id',
      'avatar',
      'name',
      'email',
      'createTime'
    ])
  },
  methods: {
    handleSuccess(response, file, fileList) {
      this.$notify({
        title: '头像修改成功',
        type: 'success',
        duration: 2500
      })
      store.dispatch('GetInfo').then(() => {})
    },
    // 监听上传失败
    handleError(e, file, fileList) {
      const msg = JSON.parse(e.message)
      this.$notify({
        title: msg.message,
        type: 'error',
        duration: 2500
      })
    },
    upLoad(file) {
      const formData = new FormData()
      formData.append('image', file.file)
      axios.put('http://127.0.0.1:8000/api/rbac/avatars/' + this.id + '/', formData, {
        headers: this.headers
      }).then((res) => {
        console.log('头像上传成功')
        this.$store.dispatch('GetInfo')
      }).catch(function(error) {
        console.log(error)
      }
      )
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss">
  .box-card{border:0;border-bottom:1px solid #ECEDFE;border-radius:unset;h4{height:26px;margin:0 0 7px;line-height:26px;font-size:1.1rem;font-weight:500;color:#444242;display:inline-block}p{font-family:Lantinghei;font-size:90%;color:#747474}ul{padding:0;margin:7px 0 0;list-style:none;font-size:80%}li{float:left;margin:0 30px 10px 0!important}li:before{width:8px;height:8px;background-color:#52acd9;color:#52acd9;display:inline-block;border-radius:50%;margin-right:5px;content:'';box-sizing:border-box}}.user-info{height:170px}.reset-email{border-bottom:0}.avatar-content,.user-info-content{float:left}.user-info-content{font-family:Lantinghei;position:relative;font-size:14px;margin:25px;div{margin-bottom:15px}}.avatar-uploader-icon{font-size:28px;width:120px;height:120px;line-height:120px;text-align:center}.avatar{width:120px;height:120px;display:block;border-radius:50%}
</style>
