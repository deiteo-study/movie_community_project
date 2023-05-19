<template>
  <div>
    <h1>Review</h1>
    <ReviewCreateView :movieId="movieId"/>
    <ReviewItemView 
    v-for = "(review, index) in reviews" :key="index"
    :review="review"/>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewCreateView from './ReviewCreateView.vue'
import ReviewItemView from './ReviewItemView.vue'

export default {
    name:'ReviewView',
    components:{
        ReviewItemView,
        ReviewCreateView
    },
    data(){
      return{
        reviews:[]
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
    } 
}
</script>

<style>

</style>