<template>
    <div class="card" @click="detail(movie.id)" >
      <img class="card-img-top" :src="poster_url" />
      <div class="card-body">
        <b class="card-title">{{ movie.title }}</b>
        <p class="card-text">{{ movie.overview }}</p>
      </div>
    </div>

</template>

<script>
export default {
    name: 'MovieItemView',
    props: {
        movie: Object,
        movies: Array,
    },
    data(){
        return {
            poster_url:`https://image.tmdb.org/t/p/w300`
        }
    },
    // this. 으로 define 오류 발생
    created(){
        this.poster_url += this.movie.poster_path
        // console.log(this.movie)
    }, 
    methods: {
        detail(movie_id){
            this.$router.push({name:'moviedetail', params:{movieId:movie_id}})
        },

    }

}

</script>

<style scoped>
img {
    height: 300px;
}
.card-text {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}
.card {
    width: 200px;
}
</style>