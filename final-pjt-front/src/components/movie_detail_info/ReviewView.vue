<template>
  <div>
    <h1>Review</h1>

    <!-- 리뷰 작성 폼  -->
    <form @submit.prevent="create_review">
      <input type="text" v-model='content' placeholder="리뷰를 작성해주세요 💬">
      <button type="submit">등록</button>
    </form>
    <br>
    <h5>[워드클라우드 들어가기]</h5>

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
        content:null,
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

<style scoped>
button {
  background-color: rgb(245, 243, 235);
  border: 1px;
  border-radius: 0.7rem;
  border-style: dotted rgb(202, 203, 172);
  width: 60px;
  height: 40px;
}

input {
  width: 300px;
  height: 50px;
  padding-left: 70px;
  margin-right: 10px;
}
</style>