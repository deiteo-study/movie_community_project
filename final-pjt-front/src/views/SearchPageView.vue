<template>
  <div>
    {{$route.query.title }}

  </div>
</template>

<script>
import axios from 'axios'


export default {
    name:'SearchPageView',
    created(){
        this.searchmovie()
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
                console.log(res)
            })
        }
    }
}
</script>

<style>

</style>