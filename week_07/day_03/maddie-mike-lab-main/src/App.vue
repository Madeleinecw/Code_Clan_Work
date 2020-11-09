<template>
  <div id="app">
    <h1>Characters</h1>
    <div class="main">
      <search-bar :characters='characters'></search-bar>
      <!-- <character-list :characters='characters'></character-list> -->
      <character-detail :character='selectedCharacter'></character-detail>
    </div>
  </div>
</template>

<script>
import CharacterList from './components/CharacterList.vue'
import CharacterDetail from './components/CharacterDetail.vue'
import { eventBus } from './main.js'
import SearchBar from './components/SearchBar.vue'

export default {
  name: 'App',
  data(){
    return {
      characters: [],
      selectedCharacter: null,
    }
  },
  components: {
    "character-list": CharacterList,
    "character-detail": CharacterDetail,
    "search-bar": SearchBar
  },
  mounted(){
    fetch('https://rickandmortyapi.com/api/character/')
    .then(res => res.json())
    .then(characters => this.characters = characters.results)
    eventBus.$on('character-select', (character) => {
      this.selectedCharacter = character
    })
  }
  
}
</script>

<style>
  body {
    background-color: antiquewhite;
  }
</style>
