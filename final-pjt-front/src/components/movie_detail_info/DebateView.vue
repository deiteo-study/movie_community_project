<template>
  <div>
    <h1>Debate Page</h1>
    <!-- 토론글 작성 -->
    <form @submit.prevent="create_opinion">
      <input type="text" @keyup.enter = "create_opinion" v-model="content" placeholder="의견을 작성해주세요">
      <button type="submit">등록</button>
    </form>
    <!-- 리뷰코드에 맞춰서 수정 -->
    <DebateItemView 
    v-for = "(debate, index) in debates" :key="index"
    :debate="debate"/>
  </div>
</template>

<script>
import axios from 'axios'
import DebateItemView from './DebateItemView.vue'

export default {
    name:'DebateView',
    components: {
      // DebateListView,
      DebateItemView,
    },
    data(){
      return {
        debates: [],
        content: null,
      }
    },
    props: {
      movieId: String
    },
    create(){
      this.get_debate()
    },
    methods: {
      get_debate(){
        // movieId 받아오기 위한 정의
        // 오류 잦음(생략으로 인한)
        const movieId = this.movieId
        axios({
          method: 'post',  // 토론글을 작성하는 요청
          url: `http://127.0.0.1:8000/api/v1/get_debate/`,
          data: {movieId}
        })
        .then(res => {
          this.debates = res.data
        })
      },
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
            this.get_debate()
          })
          .catch(err => console.log(err))
        }
      }
    }

}
</script>

<style scoped>
button {
  background-color: rgb(248, 246, 231);
  border: 1px;
  border-radius: 0.7rem;
  border-style: dotted rgb(202, 203, 172);
  width: 60px;
  height: 40px;
}

input {
  width: 300px;
  height: 50px;
  padding-left: 70px;
  margin-right: 10px;
}
</style>