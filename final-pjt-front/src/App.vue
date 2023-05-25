<template>
  <div id="app">
    <!-- 기본 네비게이션 바(홈+검색+프로필) -->
    <div v-if="$store.state.token">
      <nav>
      <router-link to="/home">
        <img src="./assets/home.png" alt="home" style="width:35px;" >
      </router-link>
      <div class="search_div">
        <input type="text" id="serch"  placeholder="검색어를 입력해주세요 :)" v-model="serach_word" 
        @keyup.enter="serach_title">
          <img src="./assets/search_icon2.png" alt="serch" style="width:25px; height:25px; margin-left:2px" class='add_cursor' @click='serach_title'> 
      </div>


      <div class="btn-group c">
        <img src="./assets/user.png" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" alt="profile" style="width:40px;" >
        <ul class="dropdown-menu">
          <li><router-link v-if='$route.fullPath.slice(1,8)=="profile"' :to="`/profile/${$store.state.my_name}`" class="dropdown-item" @click.native='$router.go()'>내 정보</router-link>
          <router-link v-else :to="`/profile/${$store.state.my_name}`" class="dropdown-item">내 정보</router-link></li>
          <li><a class="dropdown-item" href="/account/update">회원정보수정</a></li>
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
      <div class="logo" v-if="$store.state.startpage==0">
        <!-- 홈 화면 구성 -->
     
        <div class="backimg"> 
          <div class="backimgarea">
            <p class="logo-font">Cumulus</p>
          </div>
              <div class="" @click="detail(movie.id)" >
              <!-- <img class="logoimg" src="@/assets/logo11.png" alt="logo"> -->
            </div>
        </div>  
        <div class=""> 
              <button  class="logo-btn" @click="change_page1">로그인</button>
              <button class="logo-btn" @click="change_page2">회원가입</button>
            </div>
    </div>
        <!-- <img class="logoimg" src="@/assets/logo.png" alt="logo" >
        <br>
        <button  class="logo-btn" @click="change_page1">로그인</button>
        <button class="logo-btn" @click="change_page2">회원가입</button> -->
      <!-- </div> -->
      <div v-else>
        <router-view/>
        <button class="mt-2 homebtn" @click="change_home">뒤로가기</button>
      </div>
    </div>
    <button v-if="$store.state.mode" class='rounded-circle fix' @click='themeChange'>Light</button>
    <button v-else class='rounded-circle fix col_b text-white' @click='themeChange'>Dark</button>
  </div>

</template>

<script>
export default {
  name:'App',
  mounted(){
    if (this.$store.state.mode) {
      document.querySelector('#app').classList.add('text-white')
    }
  },
  created(){
    if (this.$store.state.mode) {
      document.body.classList.add('dark')
    }
    // else {
    //   document.body.classList.remove('dark')
    //   document.querySelector('#app').classList.remove('text-white')
    // }


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
    }
  },
  methods:{
    change_page1(){
      this.$store.state.startpage=1
      this.$router.push({name:'Login'})
    },
    change_page2(){
      this.$store.state.startpage=1
      this.$router.push({name:'SignUp'})
    },
    change_home(){
      this.$store.state.startpage=0
      this.$router.push({path: "/"})

    },
    logout(){
      this.$store.dispatch('logout')
    },
    // 테마 색 변경
    themeChange(){
      this.$store.commit('MODE')
      document.body.classList.toggle('dark') 
      document.querySelector('#app').classList.toggle('text-white')
    },
    serach_title(){
      if (!this.serach_word) {
        return alert('검색어를 입력해주세요!')
      }

      if (this.$route.fullPath.slice(1,7)=="search") {
        this.$router.push({ name:'search',query:{title:this.serach_word} } )
        this.serach_word=null
        this.$router.go()
      }
      else{
        this.$router.push({ name:'search',query:{title:this.serach_word} } )
        this.serach_word=null
      }

    }
  }
}

// yoon22
// gkgh0107!
</script>

<style>
hd {
  
}
body {
  -webkit-user-select:none;
  -moz-user-select:none;
  -ms-user-select:none;
  user-select:none
}
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
  height:250px;
  white-space:nowrap;
	overflow-x:scroll;
  overflow: auto;
}
.col_b {
  background-color: #121212;
  color: #ebebec;
  border-color: #bbb;
}
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  font-family: 'Do Hyeon', sans-serif;
  /* font-family: 'Sunflower', sans-serif; */
  margin-bottom: 5%;
}

.dark {
  background: #252525;
  color: #c9cccf;
}

.dark .dropdown-menu {
  background-color: rgb(108, 109, 110);
  color: #c9cccf;
}
.dark .card {
  background-color: #252525;
  color: #a3a5a8;
}
.dark a {
  /* background-color: #121212; */
  color: #a8acb0;
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
.homebtn {
  border: solid 2px gray;
  border-radius: 0.7rem;
  width: 70px;
  margin-bottom: 10px;
  cursor: pointer;
  
}
</style>

<style scoped>
.search_div{
  width:80%
  
}
input {
  width: 50%;
  height: 30px;
  border-radius: 18px;
  margin: 0 auto;
  margin-top: 5px;
  border: solid 1.5px rgb(108, 119, 127);
  padding:5px 20px;
}
input::placeholder {
    color: #d0d2d3;
    text-align: center;
}
.c {
  cursor: pointer;
}
.backimg {
  background-image: url('./assets/logo11.png');
  background-color: aliceblue;
  background-size: 2000px 1000px;
}
.backimgarea{
  height: 300px;
  padding-top: 7%;
  margin-bottom: 10px;
}
.logo {
  /* font-family: 'Hi Melody', cursive; */
  text-align: center;
  margin-top: 20%;
}
.logo-font{
  /* margin-top: 20%; */
  font-size: 59px;
  font-family: 'Caveat', cursive;
}
.logo-btn{
  border-radius: 0.6rem;
  margin: 5px;
  border: solid rgb(235, 242, 249);
  background-color: #e3eef4;
  font-size: 17px;
  width: 80px;
  height: 40px;
}


</style>

<style scoped>
.add_cursor {
  cursor: pointer;
}
div > hr {
  margin-top:0;
  margin-bottom: 0;
}
.logoimg{
  width: 100%;
  height: 60%;
  /* width: 600px;
  height: 500px; */
  /* border-radius:50%;
  box-shadow: 0 4px 6px -1px rgba(0, 0.7, 0.0, 0.1), 0 2px 4px -1px rgba(0, 0.8, 0, 0.6); */
}
.flip { 
  /* width: 700px;
  height: 650px; */
  /* top: 20%; */
  position: relative; 
  perspective: 700px;
  margin: 2rem;
  margin: 0px auto 40px auto;
}

/* .card {
  top: 20px;
  width: 500px;
  height: 500px;
  position: relative;
  transition: .0s;
  transform-style: preserve-3d;
  background-color: #fffefb;
  margin: 0px auto;
  border: none;
}  */

/* .front{
  position: absolute;
  backface-visibility: hidden;
  justify-content: center;
  align-items: center;
  color: #1f1f21;
  padding: 0px auto;
} */
/* .back {
  margin: 40px;
  backface-visibility: hidden;
} */
.logo-btn:hover {
  /* background-color:#edeee3; */
   background-color:#d2e3e7;
   border: solid rgb(181, 183, 184);
  outline: 0;
}


/* .back { 
  transform: rotateY(180deg);
}

.flip:hover .card {
  transform: rotateY(180deg);
} */
</style>