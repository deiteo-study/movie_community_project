<template>
  <div class="detail">
    <h1></h1>
    <!-- {{moviedata}} -->
    <div id="background">
      <br>
      <div class="movie_detail">

        <img class="mainimg" :src="movie_poster" height="500">

        <div class="movie_info" v-if="moviedata">
          <h2>{{ moviedata.title }}</h2>
          <div class='genres'>
            <span v-for='(genre,idx) in moviedata.genres' :key='idx'>{{genre_list[genre]}}</span>
          </div>
          <p id="score">관객 평점: {{ moviedata.vote_average }}  ⭐️⭐️⭐️</p>
          <div class="btn1" @click="movielike"> 
            <span v-if="!likes" class="bi add_cursor">🤍</span>
            <span v-else class="bi add_cursor">💖</span>
            <!-- <p v-if="!likes" class="bi bi-suit-heart"></p>
            <p v-else class="bi bi-suit-heart-fill"></p> -->
          </div>
          <p>{{ moviedata.overview }}</p>
          <div class="wrap">
          <ActorInfoView v-for="(actor,idx) in actors" :key="idx" :actor='actor' />
          </div>
        </div>
      </div>
      
      <br>
      <hr>      
    </div>
     <b>키워드 기반 유사영화 추천</b>
    <div class='fle' v-if='cc_movies'>
        <MovieItemView v-for="movie in cc_movies" :key="movie.id" :movie="movie"/>  
      </div>
      <div v-else>
        <p>리뷰가 부족해요.. ㅠㅠ</p>
      </div>
    <br>
    <hr>
    
    <div>
      <button class="btn2" @click="move_page1">예고편</button>
      <button class="btn2" @click="move_page2">영화리뷰</button>
      <button class="btn2" @click="move_page3">이미지</button>

      <img id="cursor" src="@/assets/cursor.png" alt="cursor" style="width:30px">
    </div>

    <YouTubeView v-if="page==1" :movieId='String(movieId)' />
    <ReviewView v-else-if="page==2" :movieId='String(movieId)' />
    <ImageView v-else-if="page==3" :movieId='String(movieId)' />

  </div>
</template>

<script>
import axios from 'axios'
import ActorInfoView from '@/components/actors_info/ActorInfoView'
import YouTubeView from '../components/movie_detail_info/YouTubeView.vue'
import ReviewView from '../components/movie_detail_info/ReviewView.vue'
import ImageView from '../components/movie_detail_info/ImageView.vue'
import MovieItemView from '../components/movies/MovieItemView.vue'



export default {
  name:'MovieDetail',
  components:{
    ActorInfoView,
    YouTubeView,
    ReviewView,
    ImageView,
    MovieItemView
  },
  data(){
    return{
      actors:null,
      page:1,
      likes:null,
      moviedata:null,
      movie_poster:null,
      cc_movies:null,
      genre_list:{12:'모험',14:'판타지',16:'애니메이션',18:'드라마',27:'공포',28:'액션',35:'코미디',
      36:'역사',37:'서부',53:'스릴러',80:'범죄',99:'다큐멘터리',878:'SF',9648:'미스터리',10402:'음악',
      10749:'로맨스',10751:'가족',10752:'전쟁',10770:'TV 영화'}
    }
  },
  props: {
    movieId: String,
  },
  created(){
    this.get_moviedata()
    this.recommend()
    
  },
  methods:{
    get_moviedata(){
      const movieId=this.movieId
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/${movieId}/get_movie/`,
        headers : {
          Authorization: `Token ${this.$store.state.token}`}
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
          Authorization: `Token ${this.$store.state.token}`}
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
    recommend(){
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/${this.movieId}/recommend/`
      })
      .then(res =>{
        // console.log(res.data)
        this.cc_movies=res.data
      })
    }
  },
  

}
</script>

<style scoped>
.genres {
  display: flex;
  margin: 20px 0px;

}
.genres span {
  border:1px solid black;
  margin:0 5px;
  padding:10px;
  border-radius: 0.7rem;
  background-color:grey;

}
.fle{
  display:flex;
  overflow:scroll;
}
.wrap {
  display:flex;
  width:100%;
  height:250px;
  white-space:nowrap;
	overflow-x:scroll;
  overflow: auto;
}
.mainimg {
  margin-top: 10px;
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
  padding-top: 10px;
}
.btn1{
  /* border: solid rgb(97, 114, 135); */
  border: none;
  border-radius: 30%;
  background-color: rgb(216, 223, 226);
  height: 35px;
  width: 40px;
  padding-left: 10px;
  padding-top: 5px;
  margin-bottom: 10px;
  /* padding-top: 5px;
  margin-bottom: 15px;
  padding-right: 20px; */
  /* text-align: center;
  align-content: center; */

  /* margin-bottom: 15px; */
}
.bi {
  color: rgb(220, 21, 68);
  width: 20px;
  height: 30px;
}

.btn2{
  border-radius: 0.7rem;
  border: none;
  background-color: rgb(214, 239, 239) ;
  width: 80px;
  height: 33px;
  margin: 0px 10px 10px 5px;
  
}
.btn2:hover {
  /* background-color:#edeee3; */
   background-color:#ffffff;
   border: solid rgb(211, 241, 255);
  outline: 0;
}
</style>