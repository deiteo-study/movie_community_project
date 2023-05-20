<template>
  <div id="app">
    <!-- 기본 네비게이션 바(홈+검색+프로필) -->
    <div v-if="$store.state.token">
      <nav>
      <router-link to="/home">
        <img src="./assets/home.png" alt="home" style="width:35px;" >
      </router-link>
      <input type="text" name="" id="serch"  placeholder="검색어를 입력해주세요 :)" v-model="serach_word">
        <!-- <img src="./assets/magnify.png" alt="serch" style="width:18px; height:18px" >  -->

      <div class="btn-group c">
        <img src="./assets/user.png" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" alt="profile" style="width:40px;" >
        <ul class="dropdown-menu">
          <li><router-link to="/profile" class="dropdown-item">내 정보</router-link></li>
          <li><a class="dropdown-item" href="#">회원정보수정</a></li>
          <li><hr class="dropdown-divider"></li>
          <li><p class="dropdown-item" @click='logout'>로그아웃</p></li>
        </ul>
      </div>
      
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
    <button v-if="$store.state.mode" class='rounded-circle fix' @click='themeChange'>Light</button>
    <button v-else class='rounded-circle fix col_b' @click='themeChange'>Dark</button>
  </div>

</template>

<script>
export default {
  name:'App',
  created(){
    console.log(document.querySelector('body'))
    if (this.$store.state.mode) {
      document.body.classList.add('dark')
    }
    else {
      document.body.classList.remove('dark')
    }


    if (this.$store.state.token){
      //기존 주소와 같다면 home으로 보내주기
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
      serach_word:null,
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
      this.$store.commit('LOGOUT')
    },
    themeChange(){
      this.$store.commit('MODE')
      document.body.classList.toggle('dark')
    }
  }
}
</script>

<style>
.fix {
  position: fixed;
  right:30px;
  bottom:30px;
  width: 80px;
  height: 80px;
}
.wrap {
  display:flex;
  width:100%;
  height:222px;
  white-space:nowrap;
	overflow-x:scroll;
  overflow: auto;
}
.col_b {
  background-color: #121212;
  color: #bbb;
  border-color: #bbb;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.dark {
  background: #121212;
  color: #bbb;
}

.dark .dropdown-menu {
  background-color: darkgray;
  color:white;
}
.dark .card {
  background-color: #121212;
}
.dark a {
  background-color: #121212;
}

nav {
  display: flex;
  justify-content: space-between;
  margin: 15px 50px;
 
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
  margin: 0 auto;
  border: solid 1.5px rgb(108, 119, 127);
  padding-left: 20px;
}
input::placeholder {
    color: #cccccc;
    text-align: center;
}
.c {
  cursor: pointer;
}
</style>

<style scoped>
div > hr {
  margin-top:0;
  margin-bottom: 0;
}
</style>