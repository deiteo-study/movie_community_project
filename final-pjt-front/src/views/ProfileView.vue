<template>
  <div class="profile">
    <h1>Profile</h1>
    <p>{{user.username}}</p>
    
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ProfileView',
  created(){
    axios({
      method:'get',
      url: `http://127.0.0.1:8000/accounts/user/`,
      headers : {
          Authorization: ` Token ${this.$store.state.token }`}
    })
    .then(res => {
      this.user=res.data
    })
  },
  data(){
    return {
      user:null
    }
  }
}
</script>