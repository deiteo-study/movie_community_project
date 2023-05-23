<template>
  <div v-if='review'>
    <!-- 기본 리뷰창 -->
    <!-- 개별 리뷰 클릭시 모달창으로 -->
    <div class="review">
      <p class="underline add_cursor" @click='move_profile'>작성자 : {{name}}</p>
      <!-- 구역 말고 리뷰 내용을 눌렀을때 모달창 등장 -->
      <p class="content add_cursor" @click="modalOpen">{{review.content}}</p>
      <!-- <input type="checkbox"> -->
      
      <!-- 모달 내용 -->
      
      <div class="modal-wrap" v-show="modalCheck" @click="modalOpen">
        <div class="modal-container" @click.stop="">
         <!--  모달창 content  -->
         <div @click="modalOpen">
              <img class="modal-close" src="@/assets/close.png" alt="no" style="width:20px; height:20px" >
                <!-- <button @click="modalOpen">닫기</button> -->
                <!-- <button @click="modalOpen">확인</button> -->
            </div>
         <div class="d-flex flex-row" >
            <img class="mt-1 col-3" src="@/assets/user4.png" alt="user3" style="width:35px; height:37px" >
            <div class="modal-review col-11">
                <p class="name mb-1">{{name}}</p>
          
                <p v-if='name==this.$store.state.my_name'><span @click='modify'>수정</span> <span @click='review_delete'>삭제</span></p>
                <p v-if='!update' class="mb-2 modalcontent">{{review.content}}</p>
                <p v-else class="mb-2 modalcontent">
                  <input type="text" v-model='review.content' @keyup.enter="review_update">
                  <button @click='review_update'>수정완료</button>
                </p>
                <hr>
            </div>
         </div>
            <!-- 리뷰 작성 폼 -->
            <CommentItemView
            v-for = "(comment, index) in comments" :key="index"
            :comment="comment"/>
            <div> 
                <form @submit.prevent="create_comment">
                <input class="btn1 mt-2" type="text" v-model='content' placeholder="댓글을 작성해주세요 💬"> 
                <button class="btn2" type="submit">등록</button>
                </form>
            </div>
        </div>
       </div>
<!-- 리뷰 좋아요 버튼 -->
        <span @click="reviewlike"> 
            <i v-if="!likes" class="bi bi-suit-heart"></i>
            <i v-else class="bi bi-suit-heart-fill"></i>
        </span>
    </div>
  </div>
  <div v-else>
    
  </div>
</template>

<script>
import axios from 'axios'
// import ReviewModal from './ReviewModal.vue'
import CommentItemView from './CommentItemView.vue'


export default {
    name: 'ReviewItemView',
    props: {
        reviewId: String,
    },
    components:{
        // ReviewModal,
        CommentItemView,
    },
    data(){
        return {
            comments: [],
            content: null,
            review:null,
            name:null,
            likes:null,
            // 초기값 false로 모달창 숨겨 주는 변수 선언
            // true(보일때), false(보이지 않을 때)
            modalCheck: false,
            update:false
        }
    },
    created(){
        this.get_review()
    },
    methods:{
        get_review(){
            const reviewId=this.reviewId
            axios({
                method:'get',
                url:`http://127.0.0.1:8000/api/v1/${reviewId}/get_review/`,
                headers : {
                    Authorization: ` Token ${this.$store.state.token }`}
            })
            .then(res =>{
                this.name=res.data.username
                this.review=res.data.data
                this.likes=res.data.likes
            })
        },
        reviewlike(){
            const reviewId=this.reviewId
            axios({
                method:'get',
                url:`http://127.0.0.1:8000/api/v1/${reviewId}/likes/`,
                headers : {
                    Authorization: ` Token ${this.$store.state.token }`}
            })
            .then(res =>{
            
                this.likes= res.data
            })
        },
        // 리뷰아이디를 기준으로 댓글 가져오기
        get_comment(){
          const reviewId = this.reviewId
          axios({
          method:'get',
          url:`http://127.0.0.1:8000/api/v1/${reviewId}/get_comments/`,
          })
          .then(res=>{
            this.comments=res.data
            // console.log(res.data)
          })
        },
        create_comment(){
          if(!this.content) {
            alert('리뷰에 대한 댓글을 작성해주세요')
          }
          else {
            const content = this.content
            axios({
              method: 'post',
              url:`http://127.0.0.1:8000/api/v1/${this.reviewId}/comment_create/`,
              data:{content,},
              headers : {
              Authorization: ` Token ${this.$store.state.token }`}
            })
            .then(() => {
              this.content=null
              this.get_comment()
            })
            .catch(err=>console.log(err))
          }
        },
        modalOpen(){
            // this.modalOpen=true
            this.modalCheck = !this.modalCheck
            this.get_comment()
            // document.body.classList.add('Notouch')
        },
        move_profile(){
          this.$router.push( {name:'profile', params:{username:this.name}} )
        },
        modify(){
          this.update=true
        },
        review_update(){
          const content=this.review.content
          axios({
            method:'post',
            url:`http://127.0.0.1:8000/api/v1/${this.reviewId}/review_update/`,
            data:{content,},
            headers : {
              Authorization: ` Token ${this.$store.state.token }`}
          })
          .then(() =>{
            this.update=false
          })
        },
        review_delete(){
          axios({
            method:'DELETE',
            url:`http://127.0.0.1:8000/api/v1/${this.reviewId}/review_update/`,
            headers : {
              Authorization: ` Token ${this.$store.state.token }`}
          })
          .then(() =>{
            this.modalCheck=false
            this.review=null
            alert('리뷰가 삭제되었습니다.')
          })
        }
        },
        
    }


</script>

<style>
.add_cursor {
  cursor: pointer;
}
</style>
<style>
/* 리뷰 한 칸씩 적용 */
.review{
    border: solid 1px rgb(221, 212, 212);
    border-radius: 0.9rem;
    margin: 2px auto 5px auto;
    padding: 15px 20px 0px 20px;
    width: 70%;
    font-family: 'Sunflower', sans-serif;
    
} 
.content{
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
}
/* .card-content__more-btn {
  appearance: none;
  border: none;
  padding: 0.5em;
  border-radius: 0.25em;
  cursor: pointer;
  margin: 1rem;
  color: blue;
}

.card-content__more-btn::before {
  content: '더보기';
}
.card-content__more-btn:checked::before {
  content: '닫기';
}

.content:has(+ .card-content__more-btn:checked) {
  -webkit-line-clamp:unset
} */
.modal-wrap {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
}
/* modal or popup */
.modal-container {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 550px;
  background: #fff;
  border-radius: 10px;
  padding: 8px 45px 20px 30px;
  box-sizing: border-box;
  /* margin-top: 5px; */
}
.modal-review{
    text-align: left;
    margin-left: 10px;
}
.modalcontent{
  height: 150px;
  overflow-y: scroll;
  -ms-overflow-style: none;
  margin-top: 10px;
}
.modalcontent ::-webkit-scrollbar {
    display: none;
}
.name {
    font-family: 'Sunflower', sans-serif;
    margin-top: 5px;
    margin-bottom: 10px;
}
.modal-close{
    margin-left: 100%;
    cursor: pointer;

}
.btn1{
    border-radius: 0.7rem;
    border: solid 1px rgb(177, 190, 200);
    width: 250px;
    padding-left: 20px;
}
.btn2{
    border-radius: 0.5rem;
    border: none;
    background-color: rgb(232, 239, 243);
    margin-left: 5px;
}
hr {
    width: 99%;
}
.bi {
    color: rgb(219, 45, 74);
    height: 20px;
    width: 50px;
    margin-left: 95%;
    margin-bottom: 10px;
}
</style>