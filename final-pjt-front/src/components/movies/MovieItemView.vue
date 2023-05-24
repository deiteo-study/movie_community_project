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
            <div class="back"> 
                <br>
                <b class="cardtitle">{{ movie.title }}</b>  
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
            if (this.$route.fullPath.slice(1,6)=="movie") {
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
.cardtext{
    white-space:normal;
    margin: 10px;    
    padding-top: 40px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 7;
    -webkit-box-orient: vertical;
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
  margin: 2rem;
}

.card {
  /* width: 100%; 
  height: 100%;  */
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

.front {
  /* background: tomato;  */
}

.back { 
  /* background: rgb(38, 39, 42);  */
  transform: rotateY(180deg);
}

.flip:hover .card {
  transform: rotateY(180deg);
}
</style>