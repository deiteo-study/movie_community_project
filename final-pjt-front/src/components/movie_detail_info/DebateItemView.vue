<template>
  <div>
    <p>이름: {{name}}</p>
    <p>의견: {{debate.content}}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name : 'DebateItemView',
    props: {
      debate: Object
    },
    data(){
      return {
        name:null,
      }
    },
    created(){
        this.get_username()
    },
    methods:{
        get_username(){
            const userid=this.debate.user
            axios({
                method:"get",
                url:`http://127.0.0.1:8000/accounts/${userid}/get_name/`,
            })
            .then(res => {
                this.name=res.data['name']
            })
        }
    }
}
</script>

<style>

</style>