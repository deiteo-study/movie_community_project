<template>
  <div class="detail">
    <h1>영화 상세페이지</h1>
    {{moviedata}}
    <ActorInfoView v-for="(actor,idx) in actors" :key="idx" :actor='actor' />
    <!-- <router-link :to="{ name:'youtube', params:{movieId:movieId} }">영상</router-link>
    <router-link :to="{ name:'review', params:{movieId:movieId} }">리뷰</router-link>
    <router-link :to="{ name:'image', params:{movieId:movieId} }">이미지</router-link>
    <router-link :to="{ name:'opinion', params:{movieId:movieId} }">토론</router-link> -->
    <router-view name='youtube'></router-view>
  </div>
</template>

<script>
import axios from 'axios'
import ActorInfoView from '@/components/actors_info/ActorInfoView'

export default {
  name:'MovieDetail',
  components:{
    ActorInfoView,
  },
  data(){
    return{
      actors:null
    }
  },
  props: {
    movieId: String,
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