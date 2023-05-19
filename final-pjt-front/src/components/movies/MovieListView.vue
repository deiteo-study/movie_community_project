<template>
  <div class="wrap movie active-next">
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
  components: {
    MovieItemView,
  },
  props:{
    movies:Array
  }

}

</script>

<style scoped>
.movie {
  height:400px;
  display:grid;
  margin: 0 20px;
  grid-template-columns: repeat(10,1fr);
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  margin-bottom: 50px; 
}


</style>
