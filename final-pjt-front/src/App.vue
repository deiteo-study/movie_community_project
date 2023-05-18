<template>
  <div id="app">
    <!-- 기본 네비게이션 바(홈+검색+프로필) -->
    <div v-if="$store.state.token">
      <nav>
      <router-link to="/home">
        <img src="./assets/home.png" alt="home" style="width:35px;" >
      </router-link>
      <input type="text" name="" id="serch"  placeholder="검색어를 입력해주세요 :)">
        <!-- <img src="./assets/magnify.png" alt="serch" style="width:18px; height:18px" >  -->

        <router-link to="/profile">
        <img src="./assets/user.png" alt="profile" style="width:40px;" > 
        </router-link>
        <button @click='logout'>로그아웃</button>
      
      </nav>
      <hr>
      <router-view/>
    </div>
    <!-- 로그인 -->
    <div v-else>
      <div v-if="num==0">
        <p>로고 뭐시기</p>
        <button @click="change_page1">로그인</button>
        <button @click="change_page2">회원가입</button>
      </div>
      <div v-else>
        <router-view/>
        <button @click="change_home">홈으로</button>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name:'App',
  created(){
    this.$store.dispatch('getMovies')
    if (this.$store.state.token){
      if (document.location.href=='http://localhost:8080/') {
        this.$router.push({name:'home'})
      }
    }
    else {
      // 기존에 로그인 페이지 -> 로고 페이지로 이동 했을 때 주소 변하지 않던 오류
      // 만약 되돌아 가거나, 새로고침 했을 때 주소가 default url과 다를때 강제로 이동 
      if (document.location.href!='http://localhost:8080/') {
        this.$router.push({path: "/"})
      }
    }
 
  },
  data(){
    return{
      num:0
    }
  },
  methods:{
    change_page1(){
      this.num=1
      this.$router.push({name:'Login'})
    },
    change_page2(){
      this.num=1
      this.$router.push({name:'SignUp'})
    },
    change_home(){
      this.num=0
      this.$router.push({path: "/"})

    },
    logout(){
      this.$store.dispatch('LogOUT')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  display: flex;
  justify-content: space-between;
  padding: 10px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

<style scoped>
input {
  width: 50%;
  height: 30px;
  border-radius: 18px;
  margin-left: auto;
  margin-right: auto;
  border: solid 1.5px rgb(108, 119, 127);
  padding-left: 20px;
}
input::placeholder {
    color: #cccccc;
    text-align: center;
}

</style>
