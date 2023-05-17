<template>
  <div>
    <h1>Youtube</h1>
    <iframe v-if="movie_url" :src="movie_url" frameborder="0"></iframe>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'YouTubeView',
    data(){
      return {
        movie_url:null
      }
    },
    props:{
      movieId : Number
    },
    methods:{
      get_youtube(){
        const url=`https://api.themoviedb.org/3/movie/${this.movieId}/videos?api_key=5dcc6dd1aa73987866c715e255d2af47`
        axios({
          method:'get',
          url:url,
        })
        .then(res => {
          const key=res.data.results[res.data.results.length-1].key
          this.movie_url = 'https://www.youtube.com/embed/' + key
        })

      }
    },
    created(){
      this.get_youtube()
    }
}
</script>

<style>

</style>