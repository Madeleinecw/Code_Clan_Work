<template>
  <div>
      <h3>Favourite Beers</h3>
      <ul>
      <li v-for="favouriteBeer in favouriteBeers">{{favouriteBeer.name}} <img class="small-image" :src="favouriteBeer.image_url" width ="50" height = "150"/></li>
    </ul>
  </div>
</template>

<script>
export default {
    name: 'favourite-beers',
    props: ['favouriteBeers']
}
</script>

<style>

</style>