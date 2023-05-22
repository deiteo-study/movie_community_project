<template>
    <div v-if="review" class="black_bg" >
        <div class="white-bg">
          <p>작성자 : {{name}}</p>
          <p class="content">작성내용 : {{review.content}}</p>
          <button  data-dismiss="modal">닫기</button>
          <!-- 리뷰 작성 폼 -->
            <div> 
                <form @submit.prevent="create_comment">
                  <input type="text" v-model='content' placeholder="댓글을 작성해주세요 💬">  
                  <button type="submit">등록</button>  
                </form>
            </div>
<!--  -->    
        </div>
    <!-- 모달창 내부에 댓글 -->
    <CommentItemView
    v-for = "(comment, index) in comments" :key="index"
    :comment="comment"/>
    </div>
</template>

<script>
import axios from 'axios'
import CommentItemView from './CommentItemView.vue'

export default {
    name: 'ReviewModal',
    components :{
      CommentItemView,
    },
    props: {
        reviewId: Number,
    },
    data(){
      return {
        review: null,
        name:null,
        comments: [],
        content: null,
        modalCheck: true,
      }
    },
    created(){
        this.get_review()
        this.get_comment()
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
        }
    }

}
</script>

<style scoped>
.black_bg {
    padding-top: 40px;
    background-color: rgb(232, 243, 245);
    /* position:fixed; */
    /* justify-content: center;
    align-content: center; */
    border: solid 6px rgb(165, 185, 214);
    /* position: absolute; */
    /* top: 50%;
    left: 50%; */
    width: 500px;
    height: 600px;
    margin: auto;
    position: fixed;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    border-radius: 0.9rem;
}
.content{
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 7;
    -webkit-box-orient: vertical;
}

</style>