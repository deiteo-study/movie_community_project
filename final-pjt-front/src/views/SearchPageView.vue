<template>
  <div>
    <MovieItemView v-for='movie in movies' :key='movie.id' :movie='movie'/>
  </div>
</template>

<script>
import axios from 'axios'
import MovieItemView from '../components/movies/MovieItemView.vue'


export default {
    name:'SearchPageView',
    created(){
        this.searchmovie()
    },
    components:{
        MovieItemView
    },
    data(){
        return{
            movies:null,
        }
    },
    methods:{
        searchmovie(){
            const search_title=this.$route.query.title
            axios({
                method:'POST',
                url:'http://127.0.0.1:8000/api/v1/moviesearch/',
                data:{search_title,}
            })
            .then(res => {
                this.movies=res.data
            })
        }
    }
}
</script>

<style>

</style>