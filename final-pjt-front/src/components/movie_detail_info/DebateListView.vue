<template>
  <div>
    <DebateItemView 
    v-for = "(debate, index) in debates" :key="index"
    :debate="debate"/>    
  </div>
</template>

<script>
import DebateItemView from './DebateItemView.vue'


export default {
    name: 'DebateListView',
    data(){
        return {
            debates: null
        }
    },
    // 부모인 moviedetail에서 인자 받아오기
    props: {
        movieId : Number
    },
    components: {
        DebateItemView,
    },
    created(){
        //전역변수로 actions
        this.$store.dispatch('GetDebate',this.movieId)
        this.debates=this.$store.state.debates
    }


}
</script>

<style>

</style>