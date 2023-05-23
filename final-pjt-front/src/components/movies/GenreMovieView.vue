<template>
  <div class='GenreMovie' v-if='movies'>
    
    <div class="card" v-for='movie,index in movies' :key="index" @click="detail(movie.id)">
        <img class="card-img-top" :src="poster_url+movie.poster_path" />
        <div class="card-body">
        <b class="card-title">{{ movie.title }}</b>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name:'GenreMovieView',
    props:{
        movies:Array
    },
    data(){
        return {
            poster_url:`https://image.tmdb.org/t/p/w300`,
        }
    },
    methods:{
      detail(movie_id){
            this.$router.push({name:'moviedetail', params:{movieId:String(movie_id)}})
        },
    }
}
</script>

<style>

</style>

<style scoped>
.GenreMovie{
  display:grid;
  margin: 30px 20px;
  grid-template-columns: repeat(10,1fr);
  grid-column-gap: 10px;
  grid-row-gap: 10px;

}
img {
    height: 300px;
}
.card-title {
    white-space:normal;
    margin: auto;;
  /* overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical; */
}
.card {
    width: 200px;
    height: 380px;
}
.card-body {
    display: flex;
}
</style>