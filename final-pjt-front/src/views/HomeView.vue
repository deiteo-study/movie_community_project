<template>
  <div class="home">
    <div id="main">
      <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel"  style="width:900px">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img class="d-block w-100" src="@/assets/movie2.png" alt="home" >
            <!-- <img :src="poster_url+now_playing[0]['backdrop_path']" class="d-block w-100" alt="..."> -->
            <!-- <h2>{{ now_playing[0]['title'] }}</h2> -->
          </div>
          <div class="carousel-item">
            <img class="d-block w-100 movie2" src="@/assets/movie4.png" alt="home">
            <!-- <img :src="poster_url+now_playing[1]['backdrop_path']" class="d-block w-100" alt="...">
            <h2>{{ now_playing[1]['title'] }}</h2> -->
          </div>
          <!-- <div class="carousel-item">
            <img :src="poster_url+now_playing[2]['backdrop_path']" class="d-block w-100" alt="...">
            <h2>{{ now_playing[2]['title'] }}</h2>
          </div> -->
          <!-- <div class="carousel-item">
            <img :src="poster_url+now_playing[3]['backdrop_path']" class="d-block w-100" alt="...">
            <h2>{{ now_playing[3]['title'] }}</h2>
          </div> -->
          <!-- <div class="carousel-item">
            <img :src="poster_url+now_playing[4]['backdrop_path']" class="d-block w-100" alt="...">
            <h2>{{ now_playing[4]['title'] }}</h2>
          </div> -->
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
    <div class="genrebtn">
    <button type="button" class="btn btn-outline-info" onclick = "location.href = '/movies/All' ">All</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/Comedy' ">코미디</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/ScienceFiction' ">SF</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/Fantasy' ">판타지</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/Action' ">액션</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/Crime' ">범죄</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/Thriller' ">스릴러</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/Horror' ">공포</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/Adventure' ">모험</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/Animation' ">애니메이션</button>
    <button type="button" class="btn"  onclick = "location.href = '/movies/Drama' ">드라마</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/History' ">역사</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/Western' ">서부</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/Documentary' ">다큐멘터리</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/Mystery' ">미스터리</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/Music' ">음악</button>
    <button type="button" class="btn"  onclick = "location.href = '/movies/Family' ">가족</button>
    <button type="button" class="btn" onclick = "location.href = '/movies/War' ">전쟁</button>
  </div>
    <!-- <button type="button" class="btn btn-outline-info fs-s" onclick = "location.href = '/movies/All' ">All</button>
    <button type="button" class="btn btn-outline-primary" onclick = "location.href = '/movies/Comedy' ">코미디</button>
    <button type="button" class="btn btn-outline-success" onclick = "location.href = '/movies/ScienceFiction' ">SF</button>
    <button type="button" class="btn btn-outline-danger" onclick = "location.href = '/movies/Fantasy' ">판타지</button>
    <button type="button" class="btn btn-outline-success" onclick = "location.href = '/movies/Action' ">액션</button>
    <button type="button" class="btn btn-outline-warning" onclick = "location.href = '/movies/Crime' ">범죄</button>
    <button type="button" class="btn btn-outline-info" onclick = "location.href = '/movies/Thriller' ">스릴러</button>
    <button type="button" class="btn btn-outline-primary" onclick = "location.href = '/movies/Horror' ">공포</button>
    <button type="button" class="btn btn-outline-secondary" onclick = "location.href = '/movies/Adventure' ">모험</button>
    <button type="button" class="btn btn-outline-success" onclick = "location.href = '/movies/Animation' ">애니메이션</button>
    <button type="button" class="btn btn-outline-danger" onclick = "location.href = '/movies/Drama' ">드라마</button>
    <button type="button" class="btn btn-outline-warning" onclick = "location.href = '/movies/History' ">역사</button>
    <button type="button" class="btn btn-outline-info" onclick = "location.href = '/movies/Western' ">서부</button>
    <button type="button" class="btn btn-outline-primary" onclick = "location.href = '/movies/Documentary' ">다큐멘터리</button>
    <button type="button" class="btn btn-outline-secondary" onclick = "location.href = '/movies/Mystery' ">미스터리</button>
    <button type="button" class="btn btn-outline-success" onclick = "location.href = '/movies/Music' ">음악</button>
    <button type="button" class="btn btn-outline-danger" onclick = "location.href = '/movies/Family' ">가족</button>
    <button type="button" class="btn btn-outline-warning" onclick = "location.href = '/movies/War' ">전쟁</button>
    <button type="button" class="btn btn-outline-info" onclick = "location.href = '/movies/TV_Movie' ">TV 영화</button> -->
    <!-- <button type="button" class="btn btn-outline-secondary" onclick = "location.href = '/movies/Romance' ">로맨스</button> -->
    <br>

    <p class="category">인기영화 Top10</p>
    <hr>
    <MovieListView :movies="popular_ten"/>

    <p class="category">{{$store.state.my_name}}님이 좋아할 만한 추천 영화!</p>
    <hr>
    <MovieListView :movies="recommend_movies"/>
    
    <p class="category">이런 영화는 어떤가요?</p>
    <hr>
    <MovieListView :movies="random_movies"/>

    <p class="category">{{gr1_name}} 장르 인기</p>
    <hr>
    <MovieListView :movies="gr1_movies"/>
    
    <p class="category">{{gr2_name}} 장르 인기</p>
    <hr>
    <MovieListView :movies="gr2_movies"/>


    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListView from '../components/movies/MovieListView.vue'
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
    MovieListView
  },
  data(){
    return {
      now_playing:null,
      popular_ten:null,
      random_movies:null,
      recommend_movies:null,

      gr1_name:null,
      gr1_movies:null,
      gr2_name:null,
      gr2_movies:null,
      poster_url:`https://image.tmdb.org/t/p/original`
    }
  },
  created(){
    // 현재 상영중인 영화 5개 뽑아오기
    // this.$store.commit('now_playing')
    this.$store.commit('popular_ten')
    // this.now_playing=this.$store.state.now_playing
    this.popular_ten=this.$store.state.popular_ten
    this.random_movie()
    this.recommend()
    // this.$store.dispatch('GetDBMovies')
    // this.movies=this.$store.state.movies
    if (!this.$store.state.token){
      this.$router.push({path: "/"})
    }
  },
  methods:{
    random_movie(){
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/api/v1/random/',
      })
      .then(res => {
        this.random_movies=res.data.random
        this.gr1_name=res.data.genre_random1[0]
        this.gr2_name=res.data.genre_random2[0]
        this.gr1_movies=res.data.genre_random1[1]
        this.gr2_movies=res.data.genre_random2[1]
      })
    },
    recommend(){
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/api/v1/recommendmovies/',
        headers : {
            Authorization: ` Token ${this.$store.state.token }`}
      })
      .then(res =>{
        this.recommend_movies=res.data
      })
    }
  }
}
</script>

<style scoped>
.home {
  margin-left: 35px;
  margin-right: 35px;
}
#main {
  margin-bottom:0px;
}
#carouselExampleControls{
  width: 1300px;
  margin: 0 auto;
}
img{

}
/* 
#movie1{
  width: 700px;
  height: 500px;

} */
button {
  margin: 0 10px;
  margin-bottom: 15px;
  /* font-family: 'Sunflower', sans-serif; */
}
.btn:hover {
  /* background-color:#edeee3; */
   background-color:#9bdaff;
  outline: 0;
}
h2 {
  /* font-family: 'Hi Melody', cursive; */
  /* font-family: 'Sunflower', sans-serif; */
  font-size: 45px;
}
.btn {
  /* font-family: 'Dongle', sans-serif; */
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0.7, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  cursor: pointer;
  transition: 0.5s;
  font-size: 17px;
  border-radius: 0.8rem;
  border: none; 
  background-color: rgb(225, 245, 248);
  /* font-family: 'Sunflower', sans-serif; */
}
/* 메인 홈 출력 영화 제목 */
.category{
  /* font-family: 'Dongle', sans-serif; */
  font-size: 30px;
  text-align: left;
  margin-left: 10px;
}
.genrebtn{
  margin: 0px 70px;
}

</style>
