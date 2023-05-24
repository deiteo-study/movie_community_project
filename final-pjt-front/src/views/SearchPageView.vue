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
        
    },
    methods:{
        searchmovie(){
            const search_title=this.$route.query.title
            axios({
                method:'POST',
                url:'',
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