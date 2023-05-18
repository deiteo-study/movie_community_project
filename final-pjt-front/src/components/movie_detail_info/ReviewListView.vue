<template>
  <div>
    <ReviewItemView 
    v-for = "(review, index) in reviews" :key="index"
    :review="review"/>
  </div>
</template>

<script>
import ReviewItemView from './ReviewItemView.vue'


export default {
    name: 'ReviewListView',
    data(){
        return {
            reviews:null
        }
    },
    components:{
        ReviewItemView,
    },
    created(){
        // dispatch통해서 전역변수로 보내기
        this.$store.dispatch('GetReview',this.movieId)
        this.reviews=this.$store.state.reviews
    },
    // 부모에게서 받아오는 위치
    props: {
        movieId : Number
    },
    methods: {

    }


}
</script>


<style>

</style>