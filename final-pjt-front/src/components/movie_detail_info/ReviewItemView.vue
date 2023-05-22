<template>
  <div>
    <!-- 기본 리뷰창 -->
    <!-- 개별 리뷰 클릭시 모달창으로 -->
    <div class="review" @click="modalopen">
      <p>작성자 : {{name}}</p>
      <p class="content">작성내용 : {{review.content}}</p>
    </div>
    <hr> 
    <ReviewModal v-if="modalOpen"  
    :review="review" :name='name'/>
    
  </div>
</template>

<script>
import axios from 'axios'
import ReviewModal from './ReviewModal.vue'


export default {
    name: 'ReviewItemView',
    props: {
        review: Object,
    },
    components:{
        ReviewModal,
    },
    data(){
        return {
            name:null,
            // 초기값 false로 모달창 숨겨 주는 변수 선언
            // true(보일때), false(보이지 않을 때)
            modalOpen: false,
        }
    },
    created(){
        this.get_username()
    },
    methods:{
        get_username(){
            const userid=this.review.user
            axios({
                method:"get",
                url:`http://127.0.0.1:8000/accounts/${userid}/get_name/`,
            })
            .then(res => {
                this.name=res.data['name']
            })
        },
        modalopen(){
            this.modalOpen=true
            // document.body.classList.add('Notouch')
        },
        // //data보관함에 저장된 modalopend을 함수에서 사용하기 위해 this 필수
        // close(event){
        //     // 클릭한 요소가  black-up이거나 close라면 모달창 닫기
        //     if(event.target.classList.contains('black-bg')|| event.target.classList.contains('close')){
        //         this.modalOpen = false;
        //     } 
        //     // 클릭한 class가 white라면 모달창 열기
        //     else if (event.target.classList.contains('white-bg')){
        //         this.modalOpen = true;
        //     }
        },
    }


</script>

<style scoped>
.black-bg {
  display: flex;
  align-items: center;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.432);
  position: fixed;
  padding: 20px;
}
.white-bg {
  width: 100%;
  background-color: white;
  padding: 20px;
  border-radius: 8px;
}

.close {
    cursor: pointer;
    border: none;
    background-color: #6667AB;
    border-radius: 5px;
    padding: 5px 15px;
}

.close:hover {
    color: white;
    transform: scale(1.1);
    transition: all 0.5s;
}
.Notouch {
    pointer-events: none;
}
.content{
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 7;
    -webkit-box-orient: vertical;
}
.review{
    border: solid 1px rgb(221, 212, 212);
    border-radius: 0.9rem;
}
</style>