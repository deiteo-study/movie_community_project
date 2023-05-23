<template>
  <div class="comment-list" v-if='content'>
    <p v-if='!update'><span class='add_cursor' @click='move_profile'>{{name}}</span> : {{content}}</p>
    <p v-else><span class='add_cursor' @click='move_profile'>{{name}}</span> : <input type="text" v-model='content'>
    <button @click='comment_update'>완료</button> </p>
    <p v-if='name==this.$store.state.my_name'><span @click='modify'>수정</span> 
    <span @click='comment_delete'>삭제</span></p>
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
          this.$router.push( {name:'profile', params:{username:this.name}} )
        },
      modify(){
        this.update=true
      },
      comment_update(){
          const content=this.content
          axios({
            method:'post',
            url:`http://127.0.0.1:8000/api/v1/${this.comment.id}/comment_update/`,
            data:{content,},
            headers : {
              Authorization: ` Token ${this.$store.state.token }`}
          })
          .then(() =>{
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
            this.content=null
            alert('댓글이 삭제되었습니다.')
            if (this.$route.fullPath.slice(1,8)=="profile"){
              this.$router.go()
            }
            
          })
        }

    }

}
</script>

<style scoped>
.comment-list {
  text-align: left;
  margin-left: 40px;
}

</style>