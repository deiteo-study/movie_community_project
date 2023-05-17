<template>
    <div>
        <img :src="actor_poster" alt="">
      {{ actor.name }}
    </div>
</template>

<script>
export default {
    name:'ActorInfoView',
    props:{
        actor:Object  // actor in 
    },
    data(){
        return{
            actor_poster:null,
        }
    },
    created(){
        if (this.actor.profile_path) {
            this.actor_poster= `https://image.tmdb.org/t/p/w300${this.actor.profile_path}`
        }
    }
}
</script>

<style scoped>
img {
    width: 50px;
}

</style>