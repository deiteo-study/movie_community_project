<template>
  <div v-if="review">
    <!-- 기본 리뷰창 -->
    <!-- 개별 리뷰 클릭시 모달창으로 -->
    <!-- <div class="review"> -->
      
      <!-- 구역 말고 리뷰 내용을 눌렀을때 모달창 등장 -->
      <p class="content add_cursor" @click="modalOpen">
        <span v-if='num=="0"'>- {{ review.content }}</span>
        <span v-else>- {{ comment_content }}</span></p>
      <!-- <p v-else class="content add_cursor" @click="modalOpen">- {{ comment_content }}</p> -->
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
         <div class="d-flex flex-row">
          <div class="col-8">
            <img class="mt-1" src="@/assets/user4.png" alt="user3" style="width:35px; height:37px" >
            <div class="modal-review">
                <p class="name mb-1"  @click='move_profile'>{{name}}</p>
                <hr>
                <p v-if='!update' class="mb-2 modalcontent">{{review.content}}</p>
                <p v-else class="mb-2 modalcontent">
                  <textarea class="modify-input" type="text" v-model='new_content' @keyup.enter="review_update"></textarea>
                </p>
                <hr>
                <div v-if='name==this.$store.state.my_name'>
                  <div v-if='!update'>
                    <button class="modify" @click='update=true'>수정</button> |
                    <button class="delete" @click='review_delete'>삭제</button>
                  </div>
                  <div v-else>
                    <button class="modify-btn" @click='review_update'>완료</button> |
                    <button lass="modify" @click='update=false'>취소</button>
                  </div>
                </div>
                </div>
            <br>
            </div>
                <div class="col-4">
                  <hr>
                  <div class="commentbox">
                  <CommentItemView @delete_react="get_comment"
                    v-for = "(comment, index) in comments" :key="index"
                    :comment="comment" :update="false"/>
                  </div>
                  <br>
                      <form @submit.prevent="create_comment">
                        <input class="btn1 mt-2" type="text" v-model='content' placeholder="댓글을 작성해주세요 💬"> 
                        <button class="btn2" type="submit">등록</button>
                      </form>
                  </div>
         </div>

          <!-- <div>
            <form @submit.prevent="create_comment">
              <input
                class="btn1 mt-2"
                type="text"
                v-model="content"
                placeholder="댓글을 작성해주세요 💬"
              />
              <button class="btn2" type="submit">등록</button>
            </form>
          </div> -->
        </div>
      </div>
    </div>
  <!-- </div> -->
  <div v-else></div>
</template>

<script>
import axios from "axios";
// import ReviewModal from './ReviewModal.vue'
import CommentItemView from "./CommentItemView.vue";

export default {
  name: "ReviewItemView",
  props: {
    reviewId: String,
    num:String,
    comment_content:String,
  },
  components: {
    CommentItemView,
  },
  data() {
    return {
      comments: [],
      content: null,
      review: null,
      name: null,
      likes: null,
      // 초기값 false로 모달창 숨겨 주는 변수 선언
      // true(보일때), false(보이지 않을 때)
      modalCheck: false,
      update: false,
      new_content:null,
    };
  },
  created() {
    this.get_review();
  },
  methods: {
    cuu(){
      this.$emit('cuuu')
    },
    get_review() {
      const reviewId = this.reviewId;
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/${reviewId}/get_review/`,
        headers: {
          Authorization: ` Token ${this.$store.state.token}`,
        },
      }).then((res) => {
        this.name = res.data.username;
        this.review = res.data.data;
        this.likes = res.data.likes;
      });
    },
    reviewlike() {
      const reviewId = this.reviewId;
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/${reviewId}/likes/`,
        headers: {
          Authorization: ` Token ${this.$store.state.token}`,
        },
      }).then((res) => {
        this.likes = res.data;
      });
    },
    // 리뷰아이디를 기준으로 댓글 가져오기
    get_comment() {
      // console.log(d)
      const reviewId = this.reviewId;
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/${reviewId}/get_comments/`,
      }).then((res) => {
        this.comments = res.data;
        // console.log(res.data)
      });
    },
    create_comment() {
      if (!this.content) {
        alert("리뷰에 대한 댓글을 작성해주세요");
      } else {
        const content = this.content;
        axios({
          method: "post",
          url: `http://127.0.0.1:8000/api/v1/${this.reviewId}/comment_create/`,
          data: { content },
          headers: {
            Authorization: ` Token ${this.$store.state.token}`,
          },
        })
          .then(() => {
            this.content = null;
            this.get_comment();
            this.cuu()
          })
          .catch((err) => console.log(err));
      }
    },
    modalOpen() {
      // this.modalOpen=true
      this.modalCheck = !this.modalCheck;
      this.new_content=this.review.content
      this.get_comment();
       if (!this.modalCheck) {
              this.update=false
            }
      // document.body.classList.add('Notouch')
    },
    move_profile() {
      if (this.name==this.$store.state.my_name) {
        this.$router.go()
      }
      else {
         location.href=`/profile/${this.name}`
        // this.$router.push({ name: "profile", params: { username: this.name } });
      }
      
    },
    review_update() {
      const content=this.review.content
      const new_content=this.new_content
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/api/v1/${this.reviewId}/review_update/`,
        data: { content,new_content },
        headers: {
          Authorization: ` Token ${this.$store.state.token}`,
        },
      }).then(() => {
        const content=this.review.content
        const new_content=this.new_content
        axios({
              method: "PUT",
              url: `http://127.0.0.1:8000/api/v1/${this.review.movie}/keyword/`,
              data: { content,new_content },
            }).then(() => {
            });
        this.review.content=this.new_content
        this.update = false;
      });
    },
    review_delete() {
      axios({
        method: "DELETE",
        url: `http://127.0.0.1:8000/api/v1/${this.reviewId}/review_update/`,
        headers: {
          Authorization: ` Token ${this.$store.state.token}`,
        },
      }).then(() => {
        const content=this.review.content
        const new_content=false
        axios({
              method: "PUT",
              url: `http://127.0.0.1:8000/api/v1/${this.review.movie}/keyword/`,
              data: { content,new_content },
            }).then(() => {
              this.modalCheck=false
              this.$emit('delete_react2')
              this.review=null
              alert('리뷰가 삭제되었습니다.')
            });
        // this.$router.go()
      });
    },
  },
};
</script>

<style scoped>
.add_cursor{
  cursor: pointer;
}
.review{
    text-align: left;
    border: solid 1px rgb(221, 212, 212);
    border-radius: 0.9rem;
    margin: 5px auto;
    padding: 10px 10px 0px 10px;
    width: 95%;
    
    /* font-family: 'Sunflower', sans-serif; */
    
} 
.content{
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    padding: 0 20px
}

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
  width: 1000px;
  height: 700px;
  background: #fff;
  border-radius: 10px;
  padding: 8px 45px 20px 30px;
  box-sizing: border-box;
  padding: 30px 65px 20px 65px;
  /* margin-top: 5px; */
}
.modal-review{
    text-align: left;
    margin-left: 10px;
    /* height: 700px; */
}
.modalcontent{
  height: 400px;
  overflow-y: scroll;
  -ms-overflow-style: none;
  margin-top: 20px;
  padding: 5px 10px 10px 10px;
  /* text-align: center; */
  /* position: absolute; */
  /* top: 50%; */
  /* margin-top: -25px; */
  
}
.modalcontent ::-webkit-scrollbar {
    display: none;
}
.name {
    /* font-family: 'Sunflower', sans-serif; */
    margin-top: 10px;
    margin-bottom: 20px;
    text-align: center;
}
.modal-close{
    margin-left: 95%;
    cursor: pointer;

}
.btn1{
    /* display:flex; */
    border-radius: 0.7rem;
    border: solid 1px rgb(177, 190, 200);
    width: 270px;
    height: 100px;
    margin-left: 10px;
    margin-right: 10px;
    padding: 10px;
    word-wrap:break-word;
    /* overflow:auto; */

    /* padding-left: 20px; */
}
.btn2{
    border-radius: 0.5rem;
    border: none;
    background-color: rgb(232, 239, 243);
    margin-left: 5px;
    margin-top: 5px;
  
}
hr {
    margin-left:20px;
    margin-right:20px;
}
.hd .hd2 {
    visibility: hidden;
}
.bi {
    color: rgb(219, 45, 74);
    height: 20px;
    width: 50px;
    padding-top:5px
    /* right:10px; */
    /* margin-left: 95%; */
    /* margin-bottom: 10px;  */
}
.modify{
  border: none;
  background-color: #ddf2f5;
  border-radius: 0.7rem;
  
}
.delete {
  border: none;
  background-color: rgb(245, 204, 204);
  border-radius: 0.7rem;

}
.modify-input{
  border: none;
  background-color: #e8eff0;
  border-radius: 0.7rem;
  width: 500px;
  height: 250px;
  margin-bottom: 7px;
  overflow: scroll;
  padding: 10px;

}
.modify-btn{
  border: none;
  background-color: #ddf2f5;
  border-radius: 0.7rem;
}
.commentbox{
  border: solid 0.5px rgb(235, 244, 255);
  height: 330px;
  width: 270px;
  /* margin-top: 60px; */
  margin-left: 10px;
  margin-right: 10px;
  overflow-y: scroll;
  -ms-overflow-style: none;
  padding-top: 10px;
  margin-top: 10px;
}
.col-8 {
  box-sizing: border-box;
  margin-right: 20px;
}
.col-4 {
  margin-top: 75px;
  /* margin-left: 20px; */
}
.dark .modal-wrap {
  background: rgb(177, 190, 200,0.8);
}
.dark .modal-container {
  background-color: #252525;
}
.writer {
  margin-left: 48%;
}
img {
  margin-left: 48%;
}
</style>