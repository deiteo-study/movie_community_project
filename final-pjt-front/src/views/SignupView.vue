<template>
  <div>
    <div class="main">
      <h1>Sign Up Page</h1>
      <br>
      <form @submit.prevent="signUp">
      <label for="username">username </label>
      <br>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password </label>
      <br>
      <!-- 비밀번호 확인 -->
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation </label>
      <br>
      <input type="password" id="password2" v-model="password2">
      <br>
      <div>
        <span>특수문자를 1개 이상 포함한 8자 이상의 영문,숫자로 구성해주세요 :)</span>
      </div>
      <br>
      <hr>
      <input type="submit" value="SignUp">
    </form> 
  </div>
       
  </div>
</template>

<script>
export default {
    name: 'SignupView',
    data() {
        return {
        username: null,
        password1: null,
        password2: null,
        }
    },
    methods: {
        signUp(){
            const username = this.username
            const password1 = this.password1
            const password2 = this.password2

            // 변수들 한번에 모아서
            const payload = {
                username, password1, password2
            } 
            this.$store.dispatch('signup', payload)
        },

    }


}
</script>

<style scoped>
.main {
  margin: 0 30%;
  margin-top: 15%;
}
input{
  border: solid 2px gray;
  border-radius: 0.7rem;
  width: 200px;
  margin-bottom: 10px;
  cursor: pointer;
  
}
hr{
  width: 60%;
  margin: 10px auto 10px auto;
}

span {
  font-size: 15px;
  color: rgb(180, 83, 83);
}
 
</style>