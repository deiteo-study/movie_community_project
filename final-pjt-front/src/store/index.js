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
    
    startpage:0,
    my_name:null,
    token: null,
    mode:false,
    now_playing:null,
    popular_ten:null
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    MODE(state){
      state.mode=!state.mode
    },
    now_playing(state){
      axios({
        method:'get',
        url : 'https://api.themoviedb.org/3/movie/now_playing?language=ko-KR&page=1&api_key=5dcc6dd1aa73987866c715e255d2af47'
      })
      .then(res=>{
        state.now_playing=res.data.results.slice(0,10)
        // 상세정보로 무언가 트라이할거면 밑에 코드로...
        // state.now_playing=[]
        // res.data.results.slice(0,5).forEach(element => {
        //   axios({
        //     method:'get',
        //     url:`https://api.themoviedb.org/3/movie/${element['id']}?language=ko-KR&api_key=5dcc6dd1aa73987866c715e255d2af47`
        //   })
        //   .then(res=>{
        //     state.now_playing.push(res.data)
        //     console.log(state.now_playing)
        //   })
        //   .catch(err=>console.log(err))
        // });
      })
      .catch(err => {
        console.log(err)
      })
    },

    popular_ten(state){
      axios({
        method:'get',
        url:'https://api.themoviedb.org/3/movie/popular?language=ko-kr&page=1&api_key=5dcc6dd1aa73987866c715e255d2af47'
      })
      .then(res=>{
        state.popular_ten=res.data.results.slice(0,10)
        // console.log(state.popular_ten)
      })
      .catch(err=>console.log(err))
    },


    GET_MOVIES(state,movies){
      state.movies=movies
    },
    GET_REVIEWS(state,reviews){
      state.reviews=reviews
    },
    GET_DEBATE(state, debates){
      state.debates = debates
    },
    SAVE_TOKEN(state,token) {
      state.token = token
      router.push({name:'home'})
    },
    LOGOUT(state){
      state.token=null
      state.my_name=null
      router.push({path: "/"})
    },
    MY_NAME(state,name){
      state.my_name=name
    }
  },
  actions: {
    // 회원가입 요청
    signup(context,payload){
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/signup/`,
        // signupview에서 dispatch로 보낼 때 payload로 보내줬기 때문
        data: payload
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        context.commit('MY_NAME',payload.username)
        context.state.startpage=0
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 로그인 요청
    login(context, payload){
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/login/`,
        data:payload
      })
      .then(res => {
        context.commit('SAVE_TOKEN', res.data.key)
        context.commit('MY_NAME',payload.username)
        context.state.startpage=0
      })
      .catch((err) => console.log(err))

    },
    logout(context){
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/accounts/logout/`,
        headers : {
          Authorization: ` Token ${context.state.token }`},
      })
      .then(()=>{
        context.commit('LOGOUT')
      })
      // 장고에서는 로그아웃이 되었지만 vue에서는 토큰이 남아있어서 발생하는 오류
      .catch(()=>{
        context.commit('LOGOUT')
      })
    },
    change_password(context,payload){
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/accounts/password/change/`,
        data:payload,
        headers : {
          Authorization: ` Token ${context.state.token }`},
      })
      .then(res=>{
        console.log(res)
        context.dispatch('logout')
      })
    },
    // DB로부터 
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
    // get_dbreview(context){
    //   axios({
    //     method: 'get',
    //     url:`http://127.0.0.1:8000/api/v1/get_reviews/`,
    //   })
    //   .then(res => {
    //     context.commit('GET_REVIEWS',res.data)
    //   }) 
    // },
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

