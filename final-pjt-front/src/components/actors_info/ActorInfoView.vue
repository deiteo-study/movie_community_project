<template>
    <div>
        <img v-if='actor_poster' :src="actor_poster" alt="">
        <img v-else src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973461_960_720.png" alt="">
        <p>{{ actor.name }}</p>
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
    width: 70px;
    height: 105px;
    margin: 20px;
}

</style>