<template>
  <div>
    <h1 v-if='!movies ||movies.length==0'>"{{$route.query.title}}" 의 검색 결과가 존재하지 않습니다.</h1>
    <div v-else>
        <h1>"{{$route.query.title}}" 의 검색 결과입니다.</h1>
        <p>현재 TEST DB의 데이터가 많지않은 관계 =>  적용된 유사도: 0.3△</p>
            <p>부정확한 결과가 출력될 수 있습니다.</p>
            
    </div>

    
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
            .catch(()=>{
                console.log('다시시도해라 닝겐')
            })
        }
    }
}
</script>

<style scoped>
.main {
    display: grid;
    grid-template-columns: repeat(7,1fr);

    margin: 0 10%;
    justify-content: center;
}
h1 {
    margin-top:20px;
}
</style>