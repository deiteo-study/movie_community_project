import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'  
//localStorage와 같은 기능(새로고침 방지)
// 메인

import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    movies:[
    ],
    reviews:[],
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state,movies){
      state.movies=movies
      // router.push({name:'home'})
    },
    SAVE_TOKEN(state,token) {
      state.token = token
      router.push({name:'home'})
    },
    LOGOUT(state){
      state.token=null
      router.push({name:'home'})
    },
    GET_REVIEW(state,reviews){
      state.reviews=reviews
    }
    
  },
  actions: {
    // Django DB에 저장
    saveMovies(context,data){
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

    GetDBMovies(context){
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/v1/get_movies/',
        headers : {
          Authorization: ` Token ${context.state.token }`}
      })
      .then(res=>{
        context.commit('GET_MOVIES',res.data)
      })
    },
    signUp(context,payload){
      
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/signup/`,
        // signupview에서 dispatch로 보낼 때 payload로 보내줬기 때문
        data: payload
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    trylogin(context, payload){
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/login/`,
        data:payload
      })
      .then(res => {
        context.commit('SAVE_TOKEN', res.data.key)
        console.log(res)
      })
      .catch((err) => console.log(err))

    },
    LogOUT(context){
      context.commit('LOGOUT')
    },
    // axios의 요청이 views.py의 request로 -> axios의 then으로 응답
    GetReview(context, movieId){
      axios({
        method: 'get',
        url:`http://127.0.0.1:8000/api/v1/${movieId}/review/`,
      })
      .then(res => {
        context.commit('GET_REVIEW',res.data)
      }) 
    },

  },
  modules: {
  }
})
