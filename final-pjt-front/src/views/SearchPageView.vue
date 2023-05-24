<template>
  <div>
    {{$route.query.title }}

  </div>
</template>

<script>
export default {
    name:'SearchPageView',
    created(){
        this.$store.state.movies.forEach(ele => {
            console.log(ele)
        });
    }
}
</script>

<style>

</style>