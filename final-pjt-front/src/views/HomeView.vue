<template>
  <div class="home">
    <h1>메인 홈</h1>
    <MovieListView :movies="movies"/>
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
      movies:null
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
