<template>
  <div>
    <!-- 기본 리뷰창 -->
    <!-- 개별 리뷰 클릭시 모달창으로 -->
    <div class="review">
      <p>작성자 : {{name}}</p>
      <!-- 구역 말고 리뷰 내용을 눌렀을때 모달창 등장 -->
      <p class="content" @click="modalOpen">작성내용 : {{review.content}}</p>
      
      <!-- 모달 내용 -->
      <div class="modal-wrap" v-show="modalCheck"  v-if="review" @click="modalOpen">
        <div class="modal-container" @click.stop="">
         <!--  모달창 content  -->
            <p>작성자 : {{name}}</p>
            <p class="content">작성내용 : {{review.content}}</p>
            <!-- 리뷰 작성 폼 -->
            <div> 
                <form @submit.prevent="create_comment">
                <input type="text" v-model='content' placeholder="댓글을 작성해주세요 💬"> 
                <button type="submit">등록</button>
                </form>
                <CommentItemView
    v-for = "(comment, index) in comments" :key="index"
    :comment="comment"/>
            </div>
            <div class="modal-btn">
                <button @click="modalOpen">닫기</button>
                <button @click="modalOpen">확인</button>
            </div>
        </div>
       </div>

        <button @click="reviewlike"> 
            <span v-if="!likes">좋아요</span> 
            <span v-else>좋아요 취소</span> 
        </button>
    </div>
    <!-- <ReviewModal v-if="modalOpen"  
    :reviewId="reviewId" :name='name' :modalcheck='modalcheck' />
     -->
  </div>
</template>

<script>
import axios from 'axios'
// import ReviewModal from './ReviewModal.vue'
import CommentItemView from './CommentItemView.vue'


export default {
    name: 'ReviewItemView',
    props: {
        reviewId: Number,
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
.review{
    border: solid 1px rgb(221, 212, 212);
    border-radius: 0.9rem;
} 
.modal-wrap {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
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
  padding: 20px;
  box-sizing: border-box;
}

/* .black-bg {
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
*/

</style>