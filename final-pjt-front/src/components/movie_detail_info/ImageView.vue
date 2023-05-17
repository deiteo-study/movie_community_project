<template>
  <div>
    <h1>Image</h1>
    <button @click='move1'> 옆으로 </button>
    <img :src="image_url" alt="">
    <button @click='move2'> 뒤로 </button>
  </div>
</template>

<script>
import axios from 'axios'
// import ImageItems from '@/components/movie_detail_info/ImageItems'

export default {
    name:'ImageView',
    components:{
        // ImageItems
    },
    data(){
      return {
        image_list: [],
        image_url:null,
        num:0,
      }
    },
    props:{
      movieId : Number
    },
    methods:{
      get_image(){
        const url=`https://api.themoviedb.org/3/movie/${this.movieId}/images?api_key=5dcc6dd1aa73987866c715e255d2af47`
        axios({
          method:'get',
          url:url,
        })
        .then(res => {
            const images=res.data.backdrops
            if (images.length <= 5) {
                images.forEach(ele =>{
                    this.image_list.push(ele.file_path)
                })
            }
            else {
                for (let index = 0; index < 5; index++) {
                    this.image_list.push(images[index].file_path)
                }
            }
            const image=this.image_list[this.num]
            this.image_url = `https://image.tmdb.org/t/p/w500${image}`
        })
      },
      move1(){
        if (this.num==0) {
          alert('첫 이미지입니다.')
        }
        else {
          this.num-=1
          const image=this.image_list[this.num]
          this.image_url = `https://image.tmdb.org/t/p/w500${image}`
        }
      },
      move2(){
        if (this.num==this.image_list.length-1) {
          alert('마지막 이미지입니다.')
        }
        else {
          this.num+=1
          const image=this.image_list[this.num]
          this.image_url = `https://image.tmdb.org/t/p/w500${image}`
        }
      }
    },
    created(){
      this.get_image()
    }
}
</script>

<style scoped>
img {
    width:1000px;
}
</style>