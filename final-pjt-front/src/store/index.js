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
    reviews: [],
    debates: [],
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
    GET_REVIEWS(state,reviews){
      state.reviews=reviews
    },
    GET_DEBATE(state, debates){
      state.debates = debates
    }
    
  },
  actions: {
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

    get_dbreview(context){
      axios({
        method: 'get',
        url:`http://127.0.0.1:8000/api/v1/get_reviews/`,
      })
      .then(res => {
        context.commit('GET_REVIEWS',res.data)
      }) 
    },
    // axios의 요청이 views.py의 request로 -> axios의 then으로 응답

    // 토론
    // vue에서의 axios와 index.js(여기)에서의 axios의 차이는?
    GetDebate(context, movieId){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/${movieId}/debate/`,
      })
      .then(res => {
        context.commit('GET_DEBATE', res.data)
      })
    }

  },
  modules: {
  }
})
