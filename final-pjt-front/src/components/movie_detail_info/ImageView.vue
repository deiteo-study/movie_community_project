<template>
  <div>
    <h1>Image</h1>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active" v-if="image_list[0]">
            <img :src="image_list[0]" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item" v-if="image_list[1]">
            <img :src="image_list[1]" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item" v-if="image_list[2]">
            <img :src="image_list[2]" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item" v-if="image_list[3]">
            <img :src="image_list[3]" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item" v-if="image_list[4]">
            <img :src="image_list[4]" class="d-block w-100" alt="...">
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
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
        image_list: [],     // 이미지를 불러와서 저장해줄 리스트 생성
      }
    },
    // movieId string로 받기
    props:{
      movieId : String
    },
    methods:{
      get_image(){
        const url=`https://api.themoviedb.org/3/movie/${this.movieId}/images?api_key=5dcc6dd1aa73987866c715e255d2af47`
        axios({
          method:'get',
          url:url,
        })
        .then(res => {
          // 디테일 페이지의 영화 배경 사진 받아오기
            const images=res.data.backdrops
            // 배경 사진이 5개 이하면 하나씩 돌면서 이미지 리스트에 저장하고 5개 이상이면 앞에서부터 5개씩 뽑아와서 저장하기
            if (images.length <= 5) {
                images.forEach(ele =>{
                  const image=ele.file_path
                  const image_url=`https://image.tmdb.org/t/p/w500${image}`
                  this.image_list.push(image_url)
                })
            }
            else {
                for (let index = 0; index < 5; index++) {
                  const image=images[index].file_path
                  const image_url=`https://image.tmdb.org/t/p/w500${image}`
                  this.image_list.push(image_url)   // push로 넣어준다.
                }
            }
        })
      },

    },
    created(){
      this.get_image()
    }
}
</script>

<style scoped>
img {
    width:800px;
}
#img {
  margin-bottom: 20%;
}
#carouselExampleControls {
  margin: 0 auto;
  width: 1000px;
}
</style>