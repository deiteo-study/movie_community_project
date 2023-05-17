<template>
  <div class="movie">
    <MovieItemView
    v-for="movie in movies" :key="movie.id"
    :movie="movie"
    />  
  </div>
</template>


<script>
// import axios from 'axios'

import MovieItemView from '@/components/movies/MovieItemView.vue'
 // API 불러오기
// const API_KEY = '5dcc6dd1aa73987866c715e255d2af47'
// const url = 'https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page=1&api_key='

export default {
  name: 'MovieListView',
  data(){
    return{
      movies:null
    }
  },
  components: {
    MovieItemView,
  },

  created(){
    this.movies=this.$store.state.movies
  }

}

</script>

<style scoped>
.movie {
  display:grid;
  margin:0 20%;
  grid-template-columns: repeat(3,1fr);
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  margin-bottom: 50px;
}
</style>
