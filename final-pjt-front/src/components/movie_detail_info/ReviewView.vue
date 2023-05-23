<template>
  <div>
    <h1>Review</h1>
    <div v-if='!wordcloud'>
      <h1>wordcloud를 생성할 리뷰가 없습니다. 리뷰를 작성해주세요</h1>
    </div>
    <div v-else>
      <img src='@/assets/wordcloud.png'>
    </div>
    <!-- 리뷰 작성 폼  -->
    <form @submit.prevent="create_review">
      <input type="text" v-model='content' placeholder="리뷰를 작성해주세요 💬">
      <button type="submit">등록</button>
    </form>
    <hr>
    <br>
    <h5>[워드클라우드 들어가기]</h5>

    <ReviewItemView 
    v-for = "(review, index) in reviews" :key="index"
    :reviewId="review.id"/>
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
        wordcloud:false,
      }
    },
    props:{
      movieId: String
    },
    created(){
      this.get_reviews()    
    },
    methods:{
      get_reviews(){
        const movieId= this.movieId
        axios({
          method:'get',
          url:`http://127.0.0.1:8000/api/v1/${movieId}/get_reviews/`,
        })
        .then(res=>{
          this.reviews=res.data
          this.get_wordcloud()
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
              this.make_keyword()
              // this.content=null
              this.get_reviews()
            })
            .catch(err=>console.log(err))
          }
        },
        make_keyword(){
        var content=this.content
        axios({
          method:'post',
          url:`http://127.0.0.1:8000/api/v1/${this.movieId}/keyword/`,
          data:{content,},
        })
        .then(res=>{
          console.log(res)
          this.content=null
        })

      },
      get_wordcloud(){
        const movieId=this.movieId
        axios({
          method:'get',
          url:`http://127.0.0.1:8000/api/v1/${movieId}/wordcloud/`,
        })
        .then(res =>{
          if (res.data) {
            this.wordcloud=true
          }
        })
        .catch(() => console.log('wordcloud 로드 실패'))
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
  border: solid 1px gray;
  border-radius: 0.7rem;
  width: 350px;
  height: 40px;
  padding-left: 70px;
  margin-right: 10px;
}
hr {
  width: 80%;
  margin: 20px auto 10px auto;
}
</style>