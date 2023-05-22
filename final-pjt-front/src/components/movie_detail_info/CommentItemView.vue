<template>
  <div class="comment-list">
    <p>{{name}} : {{comment.content}}</p>
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
      }
    },
    created(){
      this.get_name()
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