<template>
  <div id="app">
  <beer-list :beers='beers'></beer-list>
  <button v-if="!favouriteBeers.includes(selectedBeer)" v-on:click="addToFavourites"> Favourite Beer </button>
  <button v-if="favouriteBeers.includes(selectedBeer)" v-on:click="removeFavourite"> Delete Favourite </button>
  <beer-detail :beer='selectedBeer'></beer-detail>
  <favourite-beers :favouriteBeers='favouriteBeers'></favourite-beers>

  </div>
</template>

<script>
import BeerList from './components/BeerList.vue'
import { eventBus } from './main.js'
import BeerDetail from './components/BeerDetail.vue'
import ListItem from './components/ListItem.vue'
import FavouriteBeers from './components/FavouriteBeers.vue'

export default {
  name: 'App',
  data(){
    return{
      beers: [],
      selectedBeer: null, 
      favouriteBeers: []
    }
  },
  components: {
    "beer-list": BeerList,
    "beer-detail": BeerDetail,
    "favourite-beers": FavouriteBeers
  },
  mounted(){
    fetch('https://api.punkapi.com/v2/beers?page=2&per_page=80')
    .then(res => res.json())
    .then(data => this.beers = data)
    eventBus.$on('beer-select', (beer) => {
      this.selectedBeer = beer
    })
  },
  methods: {
    addToFavourites: function(){
        this.favouriteBeers.push(this.selectedBeer)
      },
    removeFavourite: function(){
      let index = this.favouriteBeers.indexOf(this.selectedBeer);
      this.favouriteBeers.splice(index, 1)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
