<template>
    <div class="flip">
        <div class="card" @click="detail(movie.id)" >
            <!-- 카드 앞면 -->
            <div class="front">
                <img class="card" :src="poster_url" />
                <!-- <div class="card-body"> -->
                <!-- </div> -->
            </div>
            <!-- 카드 뒷면 -->
            <div class="card back img1" :style="{ backgroundImage : `url(${poster_url})`}" > 
                <br>
                <p class="cardtitle">{{ movie.title }}</p>  
                <p class="cardtext">{{ movie.overview }}</p> 
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'MovieItemView',
    props: {
        movie: Object,
        movies: Array,
    },
    data(){
        return {
            poster_url:`https://image.tmdb.org/t/p/w300`
        }
    },
    // this. 으로 define 오류 발생
    created(){
        this.poster_url += this.movie.poster_path
        // if (this.$store.state.mode) {
        //     document.body.classList.add('dark')
        //     }
        // else {
        //     document.body.classList.remove('dark')
        //     }
        //     // console.log(this.movie)
        }, 
    methods: {
        detail(movie_id){
            if (this.$route.fullPath.slice(1,7)=="movie/") {
                this.$router.push({name:'moviedetail', params:{movieId:String(movie_id)}})
                this.$router.go()
            }
            else {
                this.$router.push({name:'moviedetail', params:{movieId:String(movie_id)}})
            }
        },
    }
}

</script>

<style scoped>
img {
    height: 300px;
    margin-bottom: 10px;
}
.cardtitle {
    white-space:normal;
    margin: auto;;
  /* overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical; */
  /* font-family: 'Sunflower', sans-serif; */
}
/* .card {
    width: 200px;
    height: 380px;
} */
.card-body {
    /* display: flex; */
}
.back p{
    color: #e9e1cc;
    /* text-align: center; */
    /* line-height: 300px;   */
    position: relative;
    }

.cardtext{
    white-space:normal;
    margin: 10px;    
    padding-top: 40px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 6;
    -webkit-box-orient: vertical;
    color: rgb(238, 228, 213);
}

* {
  margin: 0;
  padding: 0;
  list-style: none;
  box-sizing: border-box;  
  /* font-family: Pretendard; */
}

.flip { 
  width: 200px;
  height: 350px;
  position: relative; 
  perspective: 1100px;
  margin: 1rem 2rem;
  margin-bottom: 0rem;

}

.card {
  /* width: 100%; 
  height: 100%;  */
  margin-bottom: 0;
  width: 200px;
  height: 300px;
  position: relative;
  transition: .4s;
  transform-style: preserve-3d;
  background-color: #fffefb;
} 

.front, .back {
  position: absolute;
  /* width: 100%;  */
  /* height: 30px; */
  backface-visibility: hidden;
  justify-content: center;
  align-items: center;
  color: #1f1f21;
}

.back { 
  /* background: rgb(38, 39, 42, 0.8);  */
  transform: rotateY(180deg);
  background-size: cover;
/* opacity: 0.5; */
padding-bottom: 20px;
}
.back::before{
        content: "";
        opacity: 0.8;
        position: absolute;
        top: 0px;
        left: 0px;
        right: 0px;
        bottom: 0px;
        background-color: #383737;
    }

.flip:hover .card {
  transform: rotateY(180deg);
}
.img2 {
    /* background: rgba(142, 143, 146, 0.8);  */
}


</style>