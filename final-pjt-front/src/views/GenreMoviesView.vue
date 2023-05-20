<template>
  <div>
    <h1>{{ genre }}</h1>

    <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
      <input
        type="radio"
        class="btn-check"
        name="btnradio"
        id="btnradio1"
        value="true"
        autocomplete="off"
        checked
      />
      <label class="btn btn-outline-primary" for="btnradio1" @click='sort_change'>인기순</label>

      <input
        type="radio"
        class="btn-check"
        name="btnradio"
        id="btnradio2"
        
        value="false"
        autocomplete="off"
 
      />
      <label class="btn btn-outline-primary" for="btnradio2" @click='sort_change'>최신순</label>
    </div>
   
    <div>
      <GenreMovieView :movies="movie_list[page]" />
    </div>

    
    <div class='f'>
        <div>
          <ul class="pagination" v-if='page<2'>
            <li v-if='page==0' class="page-item disabled"><p class="page-link" @click='prev'>Prev</p></li>
            <li v-else class="page-item"><p class="page-link" @click='prev'>Prev</p></li>
            <li v-if='page==0' class="page-item active"><p class="page-link" @click='move_page'>1</p></li>
            <li v-else class="page-item"><p class="page-link" @click='move_page'>1</p></li>
            <li v-if='page==1' class="page-item active"><p class="page-link" @click='move_page'>2</p></li>
            <li v-else class="page-item"><p class="page-link" @click='move_page'>2</p></li>
            <li class="page-item"><p class="page-link" @click='move_page'>3</p></li>
            <li class="page-item"><p class="page-link" @click='move_page'>4</p></li>
            <li class="page-item"><p class="page-link" @click='move_page'>5</p></li>
            <li class="page-item"><p class="page-link" @click='next'>Next</p></li>
          </ul>
          <ul class="pagination" v-else-if='page > movie_list.length-3'>
            <li class="page-item"><p class="page-link" @click='prev'>Prev</p></li>
            <li class="page-item"><p class="page-link" @click='move_page'>{{movie_list.length-4}}</p></li>
            <li class="page-item"><p class="page-link" @click='move_page'>{{movie_list.length-3}}</p></li>
            <li class="page-item"><p class="page-link" @click='move_page'>{{movie_list.length-2}}</p></li>
            <li v-if='page==movie_list.length-2' class="page-item active"><p class="page-link" @click='move_page'>{{movie_list.length-1}}</p></li>
            <li v-else class="page-item"><p class="page-link" @click='move_page'>{{movie_list.length-1}}</p></li>
            <li v-if='page==movie_list.length-1' class="page-item active"><p class="page-link" @click='move_page'>{{movie_list.length}}</p></li>
            <li v-else class="page-item"><p class="page-link" @click='move_page'>{{movie_list.length}}</p></li>
            <li v-if='page==movie_list.length-1' class="page-item disabled"><p class="page-link" @click='next'>Next</p></li>
            <li v-else class="page-item"><p class="page-link" @click='next'>Next</p></li>
          </ul>
          <ul class="pagination" v-else>
            <li class="page-item"><p class="page-link" @click='prev'>Prev</p></li>
            <li class="page-item"><p class="page-link" @click='move_page'>{{page - 1}}</p></li>
            <li class="page-item"><p class="page-link" @click='move_page'>{{page}}</p></li>
            <li class="page-item active"><p class="page-link" @click='move_page'>{{page + 1}}</p></li>
            <li class="page-item"><p class="page-link" @click='move_page'>{{page + 2}}</p></li>
            <li class="page-item"><p class="page-link" @click='move_page'>{{page + 3}}</p></li>
            <li class="page-item"><p class="page-link" @click='next'>Next</p></li>
          </ul>
        </div>

        <form @submit.prevent="onemove">
            <input type="text" placeholder="이동할 페이지를 입력" v-model='movepage'>
            <button>이동</button>
        </form>
    </div>
</div>
    

</template>

<script>
import axios from "axios";
import GenreMovieView from "../components/movies/GenreMovieView.vue";

export default {
  name: "GenreMoviesView",
  props: {
    genre: String,
  },
  components: {
    GenreMovieView,
  },

  data() {
    return {
      sort_method: true,
      movie_list: null,
      page:0,
      movepage:null
    };
  },
  methods:{
    get_movies(){
        const sort_method = this.sort_method;
        var genre_id;
        if (this.genre == "All") {
        genre_id = 9999;
        } else {
        if (this.genre == "Comedy") {
            genre_id = 35;
        } else if (this.genre == "Romance") {
            genre_id = 10749;
        } else if (this.genre == "ScienceFiction") {
            genre_id = 878;
        } else if (this.genre == "Fantasy") {
            genre_id = 14;
        } else if (this.genre == "Action") {
            genre_id = 28;
        } else if (this.genre == "Crime") {
            genre_id = 80;
        } else if (this.genre == "Thriller") {
            genre_id = 53;
        } else if (this.genre == "Horror") {
            genre_id = 27;
        } else if (this.genre == "Adventure") {
            genre_id = 12;
        } else if (this.genre == "Animation") {
            genre_id = 16;
        } else if (this.genre == "Drama") {
            genre_id = 18;
        } else if (this.genre == "History") {
            genre_id = 36;
        } else if (this.genre == "Western") {
            genre_id = 37;
        } else if (this.genre == "Documentary") {
            genre_id = 99;
        } else if (this.genre == "Mystery") {
            genre_id = 9648;
        } else if (this.genre == "Music") {
            genre_id = 10402;
        } else if (this.genre == "Family") {
            genre_id = 10751;
        } else if (this.genre == "War") {
            genre_id = 10752;
        } else if (this.genre == "TV_Movie") {
            genre_id = 10770;
        }
        }
        axios({
        method: "post",
        url: `http://127.0.0.1:8000/api/v1/gernemovies/`,
        data: { genre_id, sort_method },
        })
        .then((res) => {
            this.movie_list = [];
            const cnt = Math.floor(res.data.length / 20);
            for (var i = 0; i < cnt; i++) {
            this.movie_list.push(res.data.slice(20 * i, 20 * (i + 1)));
            }
            if (cnt < res.data.length / 20) {
            this.movie_list.push(res.data.slice(20 * cnt));
            }
            this.page=0
        })
        .catch((err) => console.log(err));
    },
    prev(){
        if (this.page != 0) {
            this.page -=1
        }
    },
    move_page(event){
        this.page=Number(event.target.innerText)-1
    },
    next(){
        if (this.page != this.movie_list.length-1) {
            this.page +=1
        }
    },
    onemove(){
        if (Number(this.movepage)>this.movie_list.length){
            alert(`마지막 페이지는 ${this.movie_list.length} 입니다!
다시시도 해주세요.`)
        }
        else {
            this.page=Number(this.movepage)-1
        }
        this.movepage=null
    },
    sort_change(event){
        if (event.target.innerText=='인기순' && !this.sort_method){
            this.sort_method=true
            this.get_movies()
        }
        else if (event.target.innerText=='최신순' && this.sort_method){
            this.sort_method=false
            this.get_movies()
            
        }
    }
    
  },
  created() {
    this.get_movies()
    }
}
</script>

<style scoped>
ul {
    justify-content: center;
    cursor: pointer;
    -ms-user-select: none; 
  -moz-user-select: -moz-none;
  -khtml-user-select: none;
  -webkit-user-select: none;
  user-select: none;
}
.f {
    /* display:flex; */
    justify-content: center;
}

</style>