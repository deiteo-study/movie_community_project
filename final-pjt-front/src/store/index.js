import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies:[
    ],
    want_movies: [
    ]
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state,movies){
      state.movies=movies
    },
    ADD_WANT_MOVIE(state,title){

      for (let i=0; i<state.want_movies.length; i++) {
        if (state.want_movies[i].title==title) {
          alert('⚠ 이미 등록된 영화입니다.')
          return
        }
      }
      const is_completed = false
      state.want_movies.push({title,is_completed})

    },
    CHECK(state,want_movie){
      state.want_movies.forEach(ele =>{
        if (ele==want_movie){
          ele.is_completed=!ele.is_completed
        }
      })
    }
  },
  actions: {
    GetMovies(context){
      const url = 'https://api.themoviedb.org/3/movie/popular?language=ko-KR&page=1&api_key=5dcc6dd1aa73987866c715e255d2af47'
      axios({
        method: 'get',
        url: url,
      })
      .then(res=>{
        // 자바스크립트 슬라이싱
        context.commit('GET_MOVIES',res.data.results.slice(0,20))
      })
    },
    add_want_movie(context, title) {
      context.commit('ADD_WANT_MOVIE',title)
    },
    check(context, want_movie){
      context.commit('CHECK',want_movie)
    },
    // Moviedetail(context, movie_id){
      
    // }
  },
  modules: {
  }
})
