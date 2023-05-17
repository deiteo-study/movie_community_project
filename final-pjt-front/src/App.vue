<template>
  <div id="app">
    <nav>
      
      <router-link to="/home">
        <img src="./assets/logo.png" alt="logo" style="width:35px;" >
      </router-link>
      <input type="text" name="" id="">
      <router-link to="/profile">Profile</router-link>
    </nav>
    <hr>
    <router-view/>
  </div>
</template>

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
  width: 60%;
  border-radius: 20px;
}
</style>
