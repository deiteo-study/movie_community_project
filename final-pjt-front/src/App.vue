<template>
  <div id="app">
    <nav>
      <router-link to="/home">
        <img src="./assets/home.png" alt="home" style="width:35px;" >
      </router-link>
      <input type="text" name="" id="serch"  placeholder="검색어를 입력해주세요 :)">
        <!-- <img src="./assets/magnify.png" alt="serch" style="width:18px; height:18px" >  -->

      <router-link to="/profile">
        <img src="./assets/user.png" alt="profile" style="width:40px;" > 
      </router-link>
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
