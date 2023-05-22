<template>
  <div class="detail">
    <h1></h1>
    <!-- {{moviedata}} -->
    <div id="background">
      <br>
      <div class="movie_detail">

        <img :src="movie_poster" height="500">

        <div class="movie_info" v-if="moviedata">
          <h2>{{ moviedata.title }}</h2>
          <p id="score">관객 평점: {{ moviedata.vote_average }}  ⭐️</p>
          <button @click="movielike"> 
            <span v-if="!likes">좋아요</span> 
            <span v-else>좋아요 취소</span> 
          </button>
          <p>{{ moviedata.overview }}</p>
          <div class="wrap">
          <ActorInfoView v-for="(actor,idx) in actors" :key="idx" :actor='actor' />
          </div>
        </div>
        
      </div>
      
      <br>
      <hr>      
    </div>

  
    <br>
    <hr>
    
    <div>
      <button @click="move_page1">영상</button>
      <button @click="move_page2">리뷰</button>
      <button @click="move_page3">이미지</button>
      <!-- <button @click="move_page4">토론방</button> -->
      <img id="cursor" src="@/assets/cursor.png" alt="cursor" style="width:30px">
    </div>

    <YouTubeView v-if="page==1" :movieId='movieId' />
    <ReviewView v-else-if="page==2" :movieId='movieId' />
    <ImageView v-else-if="page==3" :movieId='movieId' />
    <!-- <DebateView v-else-if="page==4" :movieId='movieId' /> -->

  </div>
</template>

<script>
import axios from 'axios'
import ActorInfoView from '@/components/actors_info/ActorInfoView'
import YouTubeView from '../components/movie_detail_info/YouTubeView.vue'
import ReviewView from '../components/movie_detail_info/ReviewView.vue'
import ImageView from '../components/movie_detail_info/ImageView.vue'
// import DebateView from '../components/movie_detail_info/DebateView.vue'


export default {
  name:'MovieDetail',
  components:{
    ActorInfoView,
    YouTubeView,
    ReviewView,
    ImageView,
    // DebateView
  },
  data(){
    return{
      actors:null,
      page:1,
      likes:null,
      moviedata:null,
      movie_poster:null,

    }
  },
  props: {
    movieId: String,
  },
  created(){
    this.get_moviedata()
    
  },
  methods:{
    get_moviedata(){
      const movieId=this.movieId
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/${movieId}/get_movie/`,
        headers : {
          Authorization: ` Token ${this.$store.state.token }`}
      })
      .then((res)=>{
        this.moviedata=res.data.data
        this.likes=res.data.likes
        this.get_actor()
        this.movie_poster = `https://image.tmdb.org/t/p/original${this.moviedata.poster_path}`
      })
    },
    get_actor(){
      const url=`https://api.themoviedb.org/3/movie/${this.movieId}/credits?language=ko-kr&api_key=5dcc6dd1aa73987866c715e255d2af47`
      axios({
        method:'get',
        url:url,
      })
      .then(res => {
        this.actors=res.data.cast
      })
    },
    movielike(){
      const movieId=this.movieId
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/movie/${movieId}/likes/`,
        headers : {
          Authorization: ` Token ${this.$store.state.token }`}
      })
      .then(res=>{
        this.likes= res.data
      })
    },

    move_page1(){
      this.page=1
    },
    move_page2(){
      this.page=2
    },
    move_page3(){
      this.page=3
    },
    move_page4(){
      this.page=4
    },
  },
  

}
</script>

<style scoped>
.wrap {
  display:flex;
  width:100%;
  height:250px;
  white-space:nowrap;
	overflow-x:scroll;
  overflow: auto;
}
a {
  /* border: 1px solid white; */
}
a.router-link-exact-active {
  color: #42b983;
}
.movie_detail {
  display:flex;
    margin: 0 100px;
  /* border: 1px solid black; */
}

/* .movie_detail > img {
  width: 30%;
} */
.movie_info {
  width:85%;
  padding: 0 60px;
  text-align: left;;
}
h2 {
  font-size: 30px;
}
#score{
  font-size: 18px;
}
#background{
  background-color: rgb(61, 65, 68);
  color: rgb(185, 211, 222);
}
button{
  /* border: solid rgb(97, 114, 135); */
  border: none;
  border-radius: 1rem;
  background-color: rgb(234, 246, 250);
  height: 30px;
  width: 100px;
  margin-left: 3px;
  margin-right: 3px;
  margin-bottom: 20px;
}
#cursor{
}
</style>