<template>
  <div>
    <h1>Review</h1>
    <form @submit.prevent="create_review">
      <select v-model="vote">
        <option value=null>별점 Pick</option>
        <option value="0.0">0.0</option>
        <option value="0.5">0.5</option>
        <option value="1.0">1.0</option>
        <option value="1.5">1.5</option>        
        <option value="2.0">2.0</option>
        <option value="2.5">2.5</option>        
        <option value="3.0">3.0</option>
        <option value="3.5">3.5</option>
        <option value="4.0">4.0</option>
        <option value="4.5">4.5</option>
        <option value="5.0">5.0</option>
      </select>
      <input type="text" v-model='content' @keyup.enter="create_review">
      <button type="submit"></button>
    </form>
    <!-- 뒤에꺼를 앞에 담기 -->
    <ReviewListView :movieId = 'movieId'/>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewListView from './ReviewListView.vue'



export default {
    name:'ReviewView',
    components: {
      ReviewListView,
    },
    data(){
      return{
        vote:null,
        content:null,
      }
    },
    props:{
      movieId: Number
    },
    methods:{
      create_review(){
        if (!this.vote) {
          alert('별점을 선택해주세요!')
        }
        else if (!this.content) {
          alert('리뷰를 작성해주세요!')
        }
        else {
          const vote=this.vote
          const content = this.content
          axios({
            method:'post',
            url:`http://127.0.0.1:8000/api/v1/${this.movieId}/review_create/`,
            data:{vote, content,},
            headers : {
          Authorization: ` Token ${this.$store.state.token }`}
          })
          .then(res => {
            console.log(res)
          })
        }
      }
    }
}
</script>

<style>

</style>