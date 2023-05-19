<template>
  <div class="home">
    <h1>메인 홈 >>  상영중인 영화로 변경하기</h1>
    <div id="main">
      <img id="movie1" src="@/assets/movie1.png" alt="movie1">
      <!-- <img class="card-img-top" :src="poster_url" /> -->
      <!-- <router-link to="/movies">Movie</router-link> -->
      <!--코코: 354912 -->
    </div>
    <br>
    <MovieListView :movies="movies"/>
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
import MovieListView from '../components/movies/MovieListView.vue'
// @ is an alias to /src


export default {
  name: 'HomeView',
  components: {
    MovieListView
  },
  data(){
    return {
      movies:null,
      poster_url:`https://image.tmdb.org/t/p/w300`
    }
  },
  created(){
    this.$store.dispatch('GetDBMovies')
    this.movies=this.$store.state.movies
    if (!this.$store.state.token){
      this.$router.push({path: "/"})
    }
  }
}
</script>

<style scoped>
#main {
  height: 700px;
  height: 500px;
  margin-bottom: 300px;
}
/* 
#movie1{
  width: 700px;
  height: 500px;

} */
</style>
