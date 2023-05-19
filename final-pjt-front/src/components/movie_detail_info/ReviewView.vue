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
        this.$store.state.reviews.forEach(element => {
          if (element['movie']==this.movieId) {
            this.reviews.push(element)
          }
        });
        
    },    
}
</script>

<style>

</style>