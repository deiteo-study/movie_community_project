<template>
  <div>
    <h1>Image</h1>
    <!-- <ImageItems :image="image_list[0]"/> -->
    <ImageItems v-for='(image,idx) in image_list' :key="idx" :image='image' />
  </div>
</template>

<script>
import axios from 'axios'
import ImageItems from '@/components/movie_detail_info/ImageItems'

export default {
    name:'ImageView',
    components:{
        ImageItems
    },
    data(){
      return {
        image_list: [],
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
            console.log(this.image_list)
        })

      }
    },
    created(){
      this.get_image()
    }
}
</script>

<style>

</style>