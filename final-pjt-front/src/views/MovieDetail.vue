<template>
  <div class="detail">
    <h1>영화 상세페이지</h1>
    {{moviedata}}
    <ActorInfoView v-for="(actor,idx) in actors" :key="idx" :actor='actor' />
    
    <div>
      <button @click="move_page1">영상</button>
      <button @click="move_page2">리뷰</button>
      <button @click="move_page3">이미지</button>
      <button @click="move_page4">토론방</button>
    </div>
  
    <YouTubeView v-if="page==1" :movieId='movieId' />
    <ReviewView v-else-if="page==2" :movieId='movieId' />
    <ImageView v-else-if="page==3" :movieId='movieId' />
    <OpinionView v-else-if="page==4" :movieId='movieId' />

  </div>
</template>

<script>
import axios from 'axios'
import ActorInfoView from '@/components/actors_info/ActorInfoView'
import YouTubeView from '../components/movie_detail_info/YouTubeView.vue'
import ReviewView from '../components/movie_detail_info/ReviewView.vue'
import ImageView from '../components/movie_detail_info/ImageView.vue'
import OpinionView from '../components/movie_detail_info/OpinionView.vue'


export default {
  name:'MovieDetail',
  components:{
    ActorInfoView,
    YouTubeView,
    ReviewView,
    ImageView,
    OpinionView
  },
  data(){
    return{
      actors:null,
      page:1,
    }
  },
  props: {
    movieId: Number,
    moviedata:Object,
  },
  created(){
    this.get_actor()
  },
  methods:{
    get_actor(){
      const url=`https://api.themoviedb.org/3/movie/${this.movieId}/credits?language=ko-kr&api_key=5dcc6dd1aa73987866c715e255d2af47`
      axios({
        method:'get',
        url:url,
      })
      .then(res => {
        this.actors=res.data.cast
      })

    },

    move_page1(){
      this.page=1
    },
    move_page2(){
      this.page=2
    },
    move_page3(){
      this.page=3
    },
    move_page4(){
      this.page=4
    },
  },
  

}
</script>

<style scoped>
a {
  /* border: 1px solid white; */
}
a.router-link-exact-active {
  color: #42b983;
}
</style>