<template>
  <div class="comment-list" v-if='comment'>
    <p class="commentitem" v-if='!update'><span class='add_cursor' @click='move_profile'>{{name}}</span> : {{content}}</p>
    <p v-else><span class='add_cursor' @click='move_profile'>{{name}}</span> : 
    <br>
    <input type="text" v-model='content'></p>
    <div v-if='name==this.$store.state.my_name'>
      <div v-if='!update'>
        <button class="modify1" @click='update=true'>수정</button> |
        <button class="delete1" @click='comment_delete'>삭제</button>
      </div>
      <div v-else>
        <button class="delete" @click='comment_update'>완료</button> |
        <button class="modify" @click='content=comment.content, update=false'>취소</button> 
      </div>
    </div>
    <hr>
  </div>
  <div v-else>
  </div>
</template>

<script>
import axios from 'axios'


export default {
    name: 'CommentItemView',
    props:{
      comment: Object,
  
    },
    data(){
      return{
        name: null,
        update:false,
        content:null,
      }
    },
    created(){
      this.get_name()
      this.content=this.comment.content
    },
    methods: {
      abc(){
        this.update=false
      },
      get_name(){
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/${this.comment.user}/get_name/`
        })
        .then(res => {
          this.name = res.data.name
          })
      },
      move_profile(){
          if (this.$route.fullPath.slice(1,8)=='profile'){
            if (this.name==this.$route.fullPath.slice(9)) {
              this.$router.go()
            }
            else {
              location.href=`/profile/${this.name}`
            }
          }
          else{
            this.$router.push( {name:'profile', params:{username:this.name}} )
          }
        },
      comment_update(){
          const content=this.content
          if (content=='') {
            return this.comment_delete()
          }
          axios({
            method:'post',
            url:`http://127.0.0.1:8000/api/v1/${this.comment.id}/comment_update/`,
            data:{content,},
            headers : {
              Authorization: ` Token ${this.$store.state.token }`}
          })
          .then(() =>{
            this.$emit('cu')
            this.update=false
          })
        },
        comment_delete(){
          axios({
            method:'DELETE',
            url:`http://127.0.0.1:8000/api/v1/${this.comment.id}/comment_update/`,
            headers : {
              Authorization: ` Token ${this.$store.state.token }`}
          })
          .then(() =>{
            this.$emit('delete_react')
            this.$emit('cu')
            this.content=null
            alert('댓글이 삭제되었습니다.')
            // if (this.$route.fullPath.slice(1,8)=="profile"){
            //   this.$router.go()
            // }
            
          })
        }

    }

}
</script>

<style scoped>
.comment-list {
  text-align: left;
  margin-left: 40px;
  margin-bottom: 10px;
}
.modify{
  border: none;
  background-color: #ddf2f5;
  border-radius: 0.7rem;
  font-size: 13px;
}
.delete {
  border: none;
  background-color: rgb(245, 204, 204);
  border-radius: 0.7rem;
  font-size: 13px;
}
.commentitem {
  margin-bottom: 4px;
}
.modify1{
  border: none;
  background-color: #ddf2f5;
  border-radius: 0.7rem;
  font-size: 13px;
}
.delete1 {
  border: none;
  background-color: rgb(245, 204, 204);
  border-radius: 0.7rem;
  font-size: 13px;
}
input{
  border:2px solid black;
  border-radius: 0.7rem;
  padding:0 10px
}
</style>