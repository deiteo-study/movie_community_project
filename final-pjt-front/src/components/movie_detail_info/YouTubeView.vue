<template>
<!-- 영화 디테일 페이지의 youtube 예고편(컴포넌트) -->
  <div class='add_mg'>
    <div>
       <img src="@/assets/youtube.png" alt="home" style="width:45px;" >
       <h5>Youtube</h5>
    </div>
    <!-- 예고편 url이 있을 경우 가져오기 -->
    <div>
      <iframe v-if="movie_url" :src="movie_url" frameborder="0" width="1000" height="600"></iframe>
      <h1 v-else>유튜브 데이터가 없어요 :(</h1>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'YouTubeView',
    data(){
      return {
        // 초기 url값은 빈 값으로
        movie_url:null
      }
    },
    // movieId 보내주기
    props:{
      movieId : String
    },
    methods:{
      // youtube url 받아오기(get 방식)
      get_youtube(){
        const url=`https://api.themoviedb.org/3/movie/${this.movieId}/videos?language=ko-kr&api_key=5dcc6dd1aa73987866c715e255d2af47`
        axios({
          method:'get',
          url:url,
        })
        .then(res => {
          if (res.data.results.length >0) {
            for (var result of res.data.results) {
              if (result['name'].includes('예고') || result['name'].includes('공식') || result['name'].includes('티저')) {
                const key=result.key
                this.movie_url = 'https://www.youtube.com/embed/' + key     // key를 통해 영화 정보 url 완성시키기
                return
              }
            }
            this.get_youtube_us()
            
            // const key=res.data.results[res.data.results.length-1].key   // 인덱스[-1] 적용 불가
          }
        })
        .catch(()=>{})
      },
      get_youtube_us(){
        const url=`https://api.themoviedb.org/3/movie/${this.movieId}/videos?api_key=5dcc6dd1aa73987866c715e255d2af47`
        axios({
          method:'get',
          url:url,
        })
        .then(res => {
          if (res.data.results.length >0) {
            for (var result of res.data.results) {
              if (result['name'].toLowerCase().include('trailer') || result['name'].toLowerCase().include('official') || result['name'].toLowerCase().include('teaser')) {
                const key=result.key
                this.movie_url = 'https://www.youtube.com/embed/' + key     // key를 통해 영화 정보 url 완성시키기
                return
              }
            }

            
          }
        })
        .catch(()=>{})
      }
    },
    created(){
      this.get_youtube()
    }
}
</script>

<style scoped>
.add_mg{
  margin-top:50px;
  margin-bottom: 100px;;
}
img {
  margin-bottom: 5px;
}

</style>