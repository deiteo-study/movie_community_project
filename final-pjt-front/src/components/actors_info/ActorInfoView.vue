<template>
    <div>
        <img class="rounded" v-if='actor_poster' :src="actor_poster" alt="">
        <img class="rounded" v-else src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973461_960_720.png" alt="">
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
            this.actor_poster= `https://image.tmdb.org/t/p/original${this.actor.profile_path}`
        }
    }
}
</script>

<style scoped>
div {
    margin: auto;
}
img {
    width: 75px;
    height: 109px;
    margin: 10px 26px;
}
p {
    white-space:normal;
    margin: auto;
}
.round{
    border-radius: 20%;
}
p {
    font-size: 12px;
    text-align: center;
}
</style>