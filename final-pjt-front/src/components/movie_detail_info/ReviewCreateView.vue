<template>
  <div>
    <form @submit.prevent="create_review">
      <input type="text" v-model='content'>
      <button type="submit"></button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'RevieCreateView',
    data(){
        return {
            content:null
        }
    },
    props: {
        movieId : String
    },
    methods:{
      create_review(){
        if (!this.content) {
          alert('리뷰를 작성해주세요!')
        }
        else {
          const content = this.content
          axios({
            method:'post',
            url:`http://127.0.0.1:8000/api/v1/${this.movieId}/review_create/`,
            data:{content,},
            headers : {
          Authorization: ` Token ${this.$store.state.token }`}
          })
          .then(res => {
            console.log(res)
            this.content=null
            this.$store.dispatch('get_dbreview')
          })
        }
      }
    }


}
</script>


<style>

</style>