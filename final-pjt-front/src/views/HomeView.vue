<template>
  <div class="home">
    <div id="main">
      <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img :src="poster_url+now_playing[0]['backdrop_path']" class="d-block w-100" alt="...">
            <h2>{{ now_playing[0]['title'] }}</h2>
          </div>
          <div class="carousel-item">
            <img :src="poster_url+now_playing[1]['backdrop_path']" class="d-block w-100" alt="...">
            <h2>{{ now_playing[1]['title'] }}</h2>
          </div>
          <div class="carousel-item">
            <img :src="poster_url+now_playing[2]['backdrop_path']" class="d-block w-100" alt="...">
            <h2>{{ now_playing[2]['title'] }}</h2>
          </div>
          <div class="carousel-item">
            <img :src="poster_url+now_playing[3]['backdrop_path']" class="d-block w-100" alt="...">
            <h2>{{ now_playing[3]['title'] }}</h2>
          </div>
          <div class="carousel-item">
            <img :src="poster_url+now_playing[4]['backdrop_path']" class="d-block w-100" alt="...">
            <h2>{{ now_playing[4]['title'] }}</h2>
          </div>
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
    <button type="button" class="btn btn-outline-info" onclick = "location.href = '/movies/All' ">All</button>
    <button type="button" class="btn btn-outline-primary" onclick = "location.href = '/movies/Comedy' ">코미디</button>
    <!-- <button type="button" class="btn btn-outline-secondary" onclick = "location.href = '/movies/Romance' ">로맨스</button> -->
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
    <button type="button" class="btn btn-outline-info" onclick = "location.href = '/movies/TV_Movie' ">TV 영화</button>
    <br>

    <p class="category">현재 상영중인 영화 10개 출력</p>
    <hr>
    <MovieListView :movies="now_playing"/>

    <p class="category">인기영화 10개 출력</p>
    <hr>
    <MovieListView :movies="popular_ten"/>

    <hr>
  </div>
</template>

<script>
// import axios from 'axios'
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

      poster_url:`https://image.tmdb.org/t/p/original`
    }
  },
  created(){
    // 현재 상영중인 영화 5개 뽑아오기
    this.$store.commit('now_playing')
    this.$store.commit('popular_ten')
    this.now_playing=this.$store.state.now_playing
    this.popular_ten=this.$store.state.popular_ten

    // this.$store.dispatch('GetDBMovies')
    // this.movies=this.$store.state.movies
    if (!this.$store.state.token){
      this.$router.push({path: "/"})
    }
  },
  methods:{

  }
}
</script>

<style scoped>
#main {
  margin-bottom:20px;
}
#carouselExampleControls{
  width: 1300px;
  margin: 0 auto;
}
/* 
#movie1{
  width: 700px;
  height: 500px;

} */
button {
  margin: 0 10px;
  margin-bottom: 20px;
}

h2 {
  /* font-family: 'Hi Melody', cursive; */
  /* font-family: 'Sunflower', sans-serif; */
  font-size: 45px;
}
.btn {
  /* font-family: 'Dongle', sans-serif; */
  font-size: 23px;
  /* font-family: 'Sunflower', sans-serif; */
}
/* 메인 홈 출력 영화 제목 */
.category{
  /* font-family: 'Dongle', sans-serif; */
  font-size: 30px;
  text-align: left;
  margin-left: 10px;

}
</style>
