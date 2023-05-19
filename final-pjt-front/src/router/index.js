import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView,
    props:true,
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('../views/ProfileView.vue')
  },
  {
    path:'/movie/:movieId',
    name: 'moviedetail',
    component: () => import('../views/MovieDetail.vue'),
    props:true,
    // children: [
    //   {
    //     path: '',
    //     component: () => import('../components/movie_detail_info/YouTubeView.vue'),
    //   },
    //   {
    //     path: 'reviews',
    //     component: () => import('../components/movie_detail_info/ReviewView.vue'),
    //   },
    //   {
    //     path: 'image',
    //     component: () => import('../components/movie_detail_info/ImageView.vue'),
    //   },
    //   {
    //     path: 'debate',
    //     component: () => import('../components/movie_detail_info/DebateView.vue'),
    //   }
    // ]
  },
  {
    path:'/signup',
    name: 'SignUp',
    component: () => import('../views/SignupView.vue'),
  },
  {
    path:'/login',
    name: 'Login',
    component: () => import('../views/LoginView.vue'),
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
