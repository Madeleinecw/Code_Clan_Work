<template>
  <div>
    <ul>
      <form>
              <label for="beer-select">Select A Beer</label>
              <select v-on:change="handleChange" name="beer-select" id="beer-select" v-model="selectedBeer">
                  <option value="" disabled selected>Select....</option>
                  <list-item v-for="(beer, index) in beers" :beer="beer" :key="index"></list-item>
              </select>
          </form>
    </ul>
  </div>
</template>

<script>
import { eventBus } from '../main.js'
import ListItem from './ListItem.vue'

export default {
  name:'beer-list',
  data(){
    return {
      selectedBeer: null
    }
  },
  components: {
    'list-item': ListItem
  },
  props: ['beers'],
  methods: {
        handleChange(){
            eventBus.$emit('beer-select', this.selectedBeer)
        }
    }
}

</script>

<style>

</style>