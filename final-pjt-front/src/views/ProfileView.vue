<template>
  <div class="profile">
    <div v-if='userexist'>
      
      <h1 v-if='me'>내 프로필</h1>
      <h1 v-else>{{username}}님의 프로필</h1>
  
      <div>
        <b>{{username}}이 좋아요한 영화</b>
        <p v-for="(lm,idx) in user.like_movies" :key='idx'>{{lm.title}}</p>
      </div>
      <div>
        <b>{{username}}이 좋아요한 리뷰</b>
        <p v-for="(lr,idx) in user.like_reviews" :key='idx'>{{lr.content}}</p>
      </div>
      <div>
        <b>{{username}}이 작성한 리뷰</b>
        <p v-for="(wr,idx) in user.write_reviews" :key='idx'>{{wr.content}}</p>
      </div>
      <div>
        <b>{{username}}이 작성한 댓글</b>
        <p v-for="(wc,idx) in user.write_comments" :key='idx'>{{wc.content}}</p>
      </div>
 

    </div>
    <div v-else>
      <h1>존재하지 않는 유저입니다!</h1>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ProfileView',
  props:{
    username:String,
  },
  data(){
    return {
      user:null,
      userexist:true,
      me:false

    }
  },
  created(){
    this.user_check()
    // axios({
    //   method:'get',
    //   url: `http://127.0.0.1:8000/accounts/user/`,
    //   headers : {
    //       Authorization: ` Token ${this.$store.state.token }`}
    // })
    // .then(res => {
    //   this.user=res.data
    // })
  },
  methods:{
    user_check(){
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/accounts/${this.username}/get_user/`,
        headers : {
          Authorization: ` Token ${this.$store.state.token }`}
      })
      .then(res =>{
        if (res.data==false) {
          this.userexist=false
        }
        else {
          if (res.data.me) {
            this.me=true
          }
          this.user=res.data.data
        }
      })
    }
  }
}
</script>