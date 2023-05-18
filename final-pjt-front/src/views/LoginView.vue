<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="trylogin">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>    
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

        this.$store.dispatch('trylogin', payload)
    }
  }
}
</script>

<style>

</style>