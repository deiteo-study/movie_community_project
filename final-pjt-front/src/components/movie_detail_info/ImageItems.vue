<template>
    <div>
        <img :src="image_url" alt="">
    </div>
</template>

<script>
export default {
    name: 'ImageItems',
    data(){
      return {
        image_url:null
      }
    },
    props: {
        image: String
    },
    created(){
        this.image_url = `https://image.tmdb.org/t/p/original${this.image}`
    }

}
</script>

<style scoped>
img {
    width:1000px;
}
</style>