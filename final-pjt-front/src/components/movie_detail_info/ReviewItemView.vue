<template>
  <div>
    <p>이름 : {{name}}</p>
    <p>작성내용 : {{review.content}}</p>
    <hr>

  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ReviewItemView',
    props: {
        review: Object,
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
            const userid=this.review.user
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