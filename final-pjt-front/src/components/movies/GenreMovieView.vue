<template>
  <div class='GenreMovie'>
    <MovieItemView
    v-for="movie in movies" :key="movie.id"
    :movie="movie"
    />  
  </div>
</template>

<script>
import MovieItemView from './MovieItemView.vue'

export default {
    name:'GenreMovieView',
    props:{
        movies:Array
    },
    components:{
      MovieItemView
    }
}
</script>

<style>

</style>

<style scoped>
.GenreMovie{
  /* display: flex;
  white-space:normal
/*    */
  display:flex;
  flex-flow : row wrap;
  margin: 30px 20px;
  /* grid-template-columns : 1fr;
  grid-column-gap: 10px;
  grid-row-gap: 10px;  */

}
</style>