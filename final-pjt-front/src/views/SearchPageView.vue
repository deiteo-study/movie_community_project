<template>
  <div>
    <h1>{{$route.query.title}} 의 검색 결과입니다.</h1>
    
    <div class=main>
        <MovieItemView v-for='movie in movies' :key='movie.id' :movie='movie'/>
    </div>
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

<style scoped>
.main {
    display:flex;
  flex-flow : row wrap;
  margin: 0 auto;
    justify-content: center;
}
</style>