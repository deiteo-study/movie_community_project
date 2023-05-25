<template>
  <div class="movie active-next">
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
  display:flex;
	overflow:scroll;
  /* margin-right: 5px; */
  overflow-y:hidden;
}


</style>
