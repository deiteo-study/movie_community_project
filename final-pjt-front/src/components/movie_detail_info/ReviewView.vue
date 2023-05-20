<template>
  <div>
    <h1>Review</h1>

    <!-- 리뷰 작성 폼  -->
    <form @submit.prevent="create_review">
      <input type="text" v-model='content'>
      <button type="submit">리뷰작성</button>
    </form>

    <ReviewItemView 
    v-for = "(review, index) in reviews" :key="index"
    :review="review"/>
  </div>
</template>

<script>
import axios from 'axios'
// import ReviewCreateView from './ReviewCreateView.vue'
import ReviewItemView from './ReviewItemView.vue'

export default {
    name:'ReviewView',
    components:{
        ReviewItemView,
        // ReviewCreateView
    },
    data(){
      return{
        reviews:[],
        content:null
      }
    },
    props:{
      movieId: String
    },
    created(){
      this.get_review()    
    },
    methods:{
      get_review(){
        const movieId= this.movieId
        axios({
          method:'post',
          url:`http://127.0.0.1:8000/api/v1/get_review/`,
          data:{movieId,}
        })
        .then(res=>{
          this.reviews=res.data
        })
      },
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
            .then(() => {
              this.content=null
              this.get_review()
            })
            .catch(err=>console.log(err))
          }
        }
    } 
}
</script>

<style>

</style>