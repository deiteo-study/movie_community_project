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
    <button type="button" class="btn btn-outline-primary">코미디</button>
    <button type="button" class="btn btn-outline-secondary">로맨스</button>
    <button type="button" class="btn btn-outline-success">SF</button>
    <button type="button" class="btn btn-outline-danger">판타지</button>
    <button type="button" class="btn btn-outline-warning">범죄</button>
    <button type="button" class="btn btn-outline-info">스릴러</button>
    <button type="button" class="btn btn-outline-primary">공포</button>
    <button type="button" class="btn btn-outline-secondary">모험</button>
    <button type="button" class="btn btn-outline-success">애니메이션</button>
    <button type="button" class="btn btn-outline-danger">드라마</button>
    <button type="button" class="btn btn-outline-warning">역사</button>
    <button type="button" class="btn btn-outline-info">서부</button>
    <button type="button" class="btn btn-outline-primary">다큐멘터리</button>
    <button type="button" class="btn btn-outline-secondary">미스터리</button>
    <button type="button" class="btn btn-outline-success">음악</button>
    <button type="button" class="btn btn-outline-danger">가족</button>
    <button type="button" class="btn btn-outline-warning">전쟁</button>
    <button type="button" class="btn btn-outline-info">TV 영화</button>
    <br>

    <p>현재 상영중인 영화 10개 출력</p>
    <hr>
    <MovieListView :movies="now_playing"/>

    <p>인기영화 10개 출력</p>
    <hr>
    <MovieListView :movies="popular_ten"/>

    <hr>
    <!-- <MovieListView :movies="movies"/> -->
    <div class="container">
			<div class="row">
				<div class="col">
					<p><strong>Pagination</strong></p>
					<ul class="pagination">
						<li class="page-item"><a class="page-link" href="#">Previous</a></li>
						<li class="page-item"><a class="page-link" href="#">1</a></li>
						<li class="page-item"><a class="page-link" href="#">2</a></li>
						<li class="page-item"><a class="page-link" href="#">3</a></li>
						<li class="page-item"><a class="page-link" href="#">4</a></li>
						<li class="page-item"><a class="page-link" href="#">5</a></li>
						<li class="page-item"><a class="page-link" href="#">Next</a></li>
					</ul>
				</div>
			</div>
		</div>
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

      poster_url:`https://image.tmdb.org/t/p/w500`
    }
  },
  created(){
    // 현재 상영중인 영화 5개 뽑아오기
    this.$store.commit('now_playing')
    this.$store.commit('popular_ten')
    this.now_playing=this.$store.state.now_playing
    this.popular_ten=this.$store.state.popular_ten

    this.$store.dispatch('GetDBMovies')
    this.movies=this.$store.state.movies
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
</style>
