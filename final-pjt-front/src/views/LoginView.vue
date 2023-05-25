<template>
  <div class="main">
    <h1>LogIn Page</h1>
    <div class="loginform">
      <form @submit.prevent="trylogin">
        <label for="username">username : </label>
        <input type="text" id="username" v-model="username"><br>
        <br>
        <label for="password"> password : </label>
        <input type="password" id="password" v-model="password"><br>
        <br>
        <button type="submit" value="logIn">login</button>
        <br>
      </form>  
    </div>
  </div>
</template>

<script>
export default {
    name: 'LoginView',
    data() {
      return {
        username: null,
        password: null,
      }
    },
    methods: {
      trylogin() {
        const username = this.username
        const password = this.password
        if (!username) {
          alert('username을 입력해주세요')
          return
        }
        else if (!password) {
          alert('password를 입력해주세요')
          return
        }
        const payload = {
          username, password
        }

        this.$store.dispatch('login', payload)
    }
  }
}
</script>

<style scoped>
h1{
  margin-top: 8%;
}
.main {
  margin: 0 30%;
  margin-top: 15%;
}
.loginform {
  border: solid rgb(204, 206, 207) 1.5px;
  border-radius: 0.7rem;
  width: 500px;
  margin: 5% auto 0 auto;
  padding-top: 40px;
  padding-bottom: 5px;
  font-size: 18px;

}
input{
  border: solid 2px gray;
  border-radius: 0.7rem;
  width: 180px;
  margin-bottom: 10px;
  cursor: pointer;
  margin-left: 5px;
  font-size: 22px;
}
button{
  border: none;
  border-radius: 0.7rem;
  width: 53px;
  height: 30px;
  margin-bottom: 10px;
  cursor: pointer;
  background-color: rgb(224, 246, 249);
}
</style>