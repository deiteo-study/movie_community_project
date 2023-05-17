<template>
  <div class="home">
    <h1>메인 홈</h1>
    <MovieListView/>
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
  created(){
    this.$store.dispatch('GetDBMovies')
  }
}
</script>
