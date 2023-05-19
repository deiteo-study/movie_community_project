<template>
  <div class="home">
    <div id="main">
      <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="@/assets/movie1.png" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="@/assets/movie1.png" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="@/assets/movie1.png" class="d-block w-100" alt="...">
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
    <button type="button" class="btn btn-outline-primary">Primary</button>
    <button type="button" class="btn btn-outline-secondary">Secondary</button>
    <button type="button" class="btn btn-outline-success">Success</button>
    <button type="button" class="btn btn-outline-danger">Danger</button>
    <button type="button" class="btn btn-outline-warning">Warning</button>
    <button type="button" class="btn btn-outline-info">Info</button>
    <button type="button" class="btn btn-outline-primary">Primary</button>
    <button type="button" class="btn btn-outline-secondary">Secondary</button>
    <button type="button" class="btn btn-outline-success">Success</button>
    <button type="button" class="btn btn-outline-danger">Danger</button>
    <button type="button" class="btn btn-outline-warning">Warning</button>
    <button type="button" class="btn btn-outline-info">Info</button>
    <button type="button" class="btn btn-outline-primary">Primary</button>
    <button type="button" class="btn btn-outline-secondary">Secondary</button>
    <button type="button" class="btn btn-outline-success">Success</button>
    <button type="button" class="btn btn-outline-danger">Danger</button>
    <button type="button" class="btn btn-outline-warning">Warning</button>
    <button type="button" class="btn btn-outline-info">Info</button>
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
