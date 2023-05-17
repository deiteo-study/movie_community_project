import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies:[
    ],
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state,movies){
      state.movies=movies
    },
    
  },
  actions: {
    // Django DB에 저장
    saveMovies(context,data){
      console.log(context)
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/v1/save_movies/',
        data:data
      })
      .then(res=>{
        console.log(res)
      })
    },
    getMovies(context){
      const url = 'https://api.themoviedb.org/3/movie/popular?language=ko-KR&page=1&api_key=5dcc6dd1aa73987866c715e255d2af47'
      axios({
        method: 'get',
        url: url,
      })
      .then(res=>{
        const data=res.data
        context.dispatch('saveMovies',data)
      })
    },

    GetDBMovies(){
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/v1/get_movies/',
      })
      .then(res=>{
        console.log(res)
        // context.commit('GET_MOVIES')
      })
    },
  },
  modules: {
  }
})
