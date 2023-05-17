import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
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
    // children 안에서만 작동하게
    // redirec로 보내주기 ***
    // redirect:'/movie/:movieId',
    children:[
      {
        path: '',
        name: 'youtube',
        component: () => import('@/components/movie_detail_info/YouTubeView.vue'),
        props: true,
      },
      {
        path: 'review',
        name: 'review',
        component: () => import('@/components/movie_detail_info/ReviewView.vue'),
        props: true,
      },
      {
        path: 'image',
        name: 'image',
        component: () => import('@/components/movie_detail_info/ImageView.vue'),
        props: true,
      },
      {
        path: 'opinion',
        name: 'opinion',
        component: () => import('@/components/movie_detail_info/OpinionView.vue'),
        props: true,
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
