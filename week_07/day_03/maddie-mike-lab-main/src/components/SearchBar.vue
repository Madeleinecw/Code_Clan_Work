<template>
  <div class="autocomplete">
    <input @keydown.down="arrowDown" @keydown.up="arrowUp" @keydown.enter="hitEnter" v-on:input='handleChange' type="text" placeholder="Search By Name..." v-model="searchCharacter">
    <ul class="autocomplete-results" v-show="isOpen">
      <li class="autocomplete-result" v-for="(result, i) in results" :key="i" @click="setResult(result)" :class="{ 'is-active': i === arrowCounter }">{{result.name}}</li>
    </ul>
  </div>
</template>

<script>
import { eventBus } from '../main.js'

export default {
    name:'search-bar',
    props: ['characters'],
    data(){
        return {
            searchCharacter: null,
            results: [],
            isOpen: false,
            arrowCounter: -1
        }
    },
    mounted() {
        document.addEventListener('click', this.handleClickOutside);
    },
    methods: {
        handleChange(){
            this.isOpen = true
            this.filterResults();
        },
        filterResults(){
            this.results = this.characters.filter(character => character.name.toLowerCase().indexOf(this.searchCharacter.toLowerCase()) > -1)
        },
        setResult(result){
            this.searchCharacter = result.name
            this.isOpen = false
            for (let character of this.characters){
                if (character.name.toLowerCase() === this.searchCharacter.toLowerCase()){
                    eventBus.$emit('character-select', character)
                }
            }
            this.searchCharacter = ""
        },
        arrowDown(){
            if(this.arrowCounter < this.results.length){
                this.arrowCounter += 1
            }
        },
        arrowUp(){
            if (this.arrowCounter > 0) {
                this.arrowCounter -= 1;
            }
        },
        hitEnter(){
            this.searchCharacter = this.results[this.arrowCounter].name;
            this.isOpen = false;
            for (let character of this.characters){
                if (character.name.toLowerCase() === this.searchCharacter.toLowerCase()){
                    eventBus.$emit('character-select', character)
                }
            }
            this.arrowCounter = -1;
            this.searchCharacter = ""
        },
        handleClickOutside(evt) {
            if (!this.$el.contains(evt.target)) {
              this.isOpen = false;
              this.arrowCounter = -1;
            }
        }
    }
}

</script>

<style>
    .autocomplete {
    position: relative;
    width: 130px;
  }

  .autocomplete-results {
    padding: 0;
    margin: 0;
    border: 1px solid #eeeeee;
    height: 120px;
    overflow: auto;
  }

  .autocomplete-result {
    list-style: none;
    text-align: left;
    padding: 4px 2px;
    cursor: pointer;
  }

  .autocomplete-result.is-active,
  .autocomplete-result:hover {
    background-color: #4AAE9B;
    color: white;
  }
</style>