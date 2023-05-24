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
    path: '/profile/:username',
    name: 'profile',
    component: () => import('../views/ProfileView.vue'),
    props:true,
  },
  {
    path:'/movie/:movieId',
    name: 'moviedetail',
    component: () => import('../views/MovieDetailView.vue'),
    props:true,
  },
  {
    path: '/movies/:genre',
    name: 'genremovies',
    component: () => import('../views/GenreMoviesView.vue'),
    props:true
  },
  {
    path:'/signup',
    name: 'SignUp',
    component: () => import('../views/SignupView.vue'),
  },
  {
    path:'/login/',
    name: 'Login',
    component: () => import('../views/LoginView.vue'),
  },
  {
    path:'/account/update',
    name:'accountupdate',
    component: () => import('../views/AccountUpdateView.vue'),
  },
  {
    path:'/search',
    name:'search',
    component: () => import('../views/SearchPageView.vue'),
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
