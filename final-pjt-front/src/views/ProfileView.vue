<template>
  <div class="profile">
    <div v-if='userexist'>
      <br>
      <h2 v-if='me'>My Profile</h2>
      <h2 v-else>{{username}}님의 프로필</h2>
      <p> 임시로 구조 짜놓은 디자인!</p>
      <p> 댓글 단게 너무 많으면 더보기로 줄일지! 고민</p>
      <div>
        <img src="@/assets/user5.png" alt="home" style="width:170px; height:170px;" >
        <span><p>followers: 00  | followings: 00</p></span>
      </div>
      <hr>
      
      <h5>☃︎{{username}}이 좋아한 영화</h5>
        <div class="box1">
          <p v-for="(lm,idx) in user.like_movies" :key='idx' class='add_cursor' @click='move_movie(lm.id)'>- {{lm.title}}</p>
        </div>
      
      <h5>☃︎{{username}}이 좋아한 리뷰</h5>
        <div class="box2">
          <p v-for="(lr,idx) in user.like_reviews" :key='idx' class='add_cursor' @click='move_review(lm.id)'>- {{lr.content}}</p>
        </div>
      
        <h5>☃︎{{username}}이 작성한 리뷰</h5>
          <div class="box1">
            <p v-for="(wr,idx) in user.write_reviews" :key='idx' class='add_cursor' @click='move_review(lm.id)'>- {{wr.content}}</p>
        </div>
      
        <h5>☃︎{{username}}이 작성한 댓글</h5>
          <div class="box2">
            <p v-for="(wc,idx) in user.write_comments" :key='idx'>- {{wc.content}}</p>
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
    },
    move_movie(movieId){
      this.$router.push({name:'moviedetail', params:{movieId:movieId}})
    },
    move_review(){

    }
  }
}
</script>

<style scoped>
h5 {
  /* font-family: 'Dongle', sans-serif; */
  font-family: 'Gaegu', cursive;
  /* font-family: 'Hi Melody', cursive; */
  /* font-family: 'Sunflower', sans-serif; */
  text-align: left;
  margin-left: 220px;
  margin-top: 5px;
}

img {
  margin-bottom: 10px;
}
hr {
  width: 70%;
  margin: auto;
}
.box1 {
  width: 70%;
  border: solid 1px rgb(172, 172, 201);
  border-radius: 0.7rem;
  margin: 10px auto 20px auto;
  padding: 10px 20px;
  text-align: left;
  
}

.box2 {
  width: 70%;
  border: none;
  border-radius: 0.7rem;
  background-color: rgb(232, 239, 246);
  margin: 10px auto 20px auto;
  padding: 10px 20px;
  text-align: left;
}
</style>