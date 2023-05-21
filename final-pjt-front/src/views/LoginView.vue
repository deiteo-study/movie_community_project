<template>
  <div>
    <h1>LogIn Page</h1>
    <h5>[나중에 꾸미기]</h5>
    <div class="loginform">
      <form @submit.prevent="trylogin">
        <label for="username">username : </label>
        <input type="text" id="username" v-model="username"><br>
        <br>
        <label for="password"> password : </label>
        <input type="password" id="password" v-model="password"><br>
        <br>
        <input type="submit" value="logIn">
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
.loginform {
  border: solid gray;
  border-radius: 0.7rem;
  width: 500px;
  margin: 5% auto 0 auto;
  padding-top: 40px;
  padding-bottom: 5px;

}

</style>