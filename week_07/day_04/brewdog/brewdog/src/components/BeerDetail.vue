<template>
  <div v-if="beer">
  <h3>{{beer.name}}</h3>
  <p> {{beer.tagline}} </p>
  <p> Description: {{beer.description}} </p>
  <p> Since: {{beer.first_brewed}}</p>
  <img :src="beer.image_url">
  </div>
</template>

<script>
export default {
    name: 'beer-detail',
    props: ['beer']
}
</script>

<style>

</style>