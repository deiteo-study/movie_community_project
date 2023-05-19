<template>
  <div class="detail">
    <h1></h1>
    <!-- {{moviedata}} -->
    <div id="background">
      <br>
      <div class="movie_detail">
      <img :src="movie_poster" alt="">
        <div class="movie_info">
          <h2>{{ moviedata.title }}</h2>
          <p id="score">관객 평점: {{ moviedata.vote_average }}  ⭐️</p>
          <p>{{ moviedata.overview }}</p>
        </div>
      </div>
      <br>
      <hr>      
    </div>

    <div class="movie_detail1">
      <ActorInfoView v-for="(actor,idx) in actors" :key="idx" :actor='actor' />
    </div>
    <br>
    <hr>
    
    <div>
      <button @click="move_page1">영상</button>
      <button @click="move_page2">리뷰</button>
      <button @click="move_page3">이미지</button>
      <button @click="move_page4">토론방</button>
      <img id="cursor" src="@/assets/cursor.png" alt="cursor" style="width:30px">
    </div>

    <!-- <router-link :to='link1'>영상</router-link>
    <router-link :to='link2'>리뷰</router-link>
    <router-link :to='link3'>이미지</router-link>
    <router-link :to='link4'>토론</router-link> 
    <router-view></router-view> -->
    <YouTubeView v-if="page==1" :movieId='movieId' />
    <ReviewView v-else-if="page==2" :movieId='movieId' />
    <ImageView v-else-if="page==3" :movieId='movieId' />
    <DebateView v-else-if="page==4" :movieId='movieId' />

  </div>
</template>

<script>
import axios from 'axios'
import ActorInfoView from '@/components/actors_info/ActorInfoView'
import YouTubeView from '../components/movie_detail_info/YouTubeView.vue'
import ReviewView from '../components/movie_detail_info/ReviewView.vue'
import ImageView from '../components/movie_detail_info/ImageView.vue'
import DebateView from '../components/movie_detail_info/DebateView.vue'


export default {
  name:'MovieDetail',
  components:{
    ActorInfoView,
    YouTubeView,
    ReviewView,
    ImageView,
    DebateView
  },
  data(){
    return{
      actors:null,
      page:1,
      movie_poster:null,
      moviedata:null,

      // link1:null,
      // link2:null,
      // link3:null,
      // link4:null,
    }
  },
  props: {
    movieId: String,
  },
  created(){
    // this.link1='/movie/'+this.movieId
    // this.link2='/movie/'+this.movieId +'/reviews'
    // this.link3='/movie/'+this.movieId +'/image'
    // this.link4='/movie/'+this.movieId +'/debate'


    this.get_moviedata()
    this.get_actor()
    this.$store.dispatch('get_dbreview')
    this.movie_poster = `https://image.tmdb.org/t/p/w300${this.moviedata.poster_path}`
  },
  methods:{
    get_moviedata(){
      for (var movie of this.$store.state.movies) {
        if (movie['id']==this.movieId){
          this.moviedata=movie
          return
        }
      }

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
.movie_detail1 {
  display:flex;
}
.movie_detail > img {
  width: 30%;
}
.movie_info {
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
  width: 70px;
  margin-left: 3px;
  margin-right: 3px;
}
#cursor{
}
</style>