<template>
  <div>
    <h1>Debate Page</h1>
    <form @submit.prevent="create_opinion">
      <input type="text" @keyup.enter = "create_opinion" v-model="content">
      <button type="submit"></button>
    </form>
    <DebateListView :movieId="movieId"/>
  </div>
</template>

<script>
import axios from 'axios'
import DebateListView from './DebateListView.vue'

export default {
    name:'DebateView',
    components: {
      DebateListView,
    },
    data(){
      return {
        content: null,
      }
    },
    props: {
      movieId: String

    },
    methods: {
      create_opinion(){
        if (!this.content){
          alert('의견을 작성해주세요!')
        }
        else {
          const content = this.content
          axios({
            method: 'post',
            url: `http://127.0.0.1:8000/api/v1/${this.movieId}/debate_create/`,
            data: {
              content,
              },
            headers : {
              Authorization: ` Token ${this.$store.state.token }`}
          })
          .then(res => {
            console.log(res)
          })
        }
      }
    }

}
</script>

<style>

</style>