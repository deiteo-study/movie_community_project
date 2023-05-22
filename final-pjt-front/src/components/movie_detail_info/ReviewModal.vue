<template>
    <div class="black_bg" >
        <div class="white-bg">
          <p>작성자 : {{name}}</p>
          <p class="content">작성내용 : {{review.content}}</p>
            <div>
                <input type="text" v-model='content' placeholder="댓글을 작성해주세요 💬">  
                <button type="submit" class="">등록</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ReviewModal',
    props: {
        review: Object,
        name:String,
    },

    methods: {

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