<template>
  <div id="app">
    <h2>Global population:  </h2>

    <label for="country_select">Select a Country:</label>
    <select id="country_select" v-model="selectedCountry" >
      <option disabled value="">Select a country</option>
      <option v-for="country in countries"  :value="country">{{country.name}}</option>
    </select>

    <country-detail></country-detail>

    <button>Add Country</button>

    <favourite-countries></favourite-countries>
</div>

</template>

<script>
import CountryDetail from './components/CountryDetail.vue';
import FavouriteListItem from './components/FavouriteListItem.vue';

export default {
  name: 'App',
  props:[],
  data() {
    return {
      countries: [],
      selectedCountry: null,
      favouriteCountries: [],
      worldPopulation: null
    }
  },
  components: {
    'country-detail': CountryDetail,
    'favourite-countries': FavouriteListItem,
    
  },
    computed: {

    },
    mounted(){
      this.fetchCountries()
    },
    methods: {
      fetchCountries: function(){
    const request = fetch("https://restcountries.eu/rest/v2/all")
    .then(response => response.json())
    .then(data => this.countries = data)
},
}
}
</script>

<style>
.small-flag {
  height: 20px
}

.selected-country {
  color: green;
}

</style>
