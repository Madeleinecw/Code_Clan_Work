<template>
  <div>
      <ul>
          <form>
              <label for="character-select">Select A Character</label>
              <select v-on:change="handleChange" name="character-select" id="character-select" v-model="selectedCharacter">
                  <option value="" disabled selected>Select....</option>
                  <list-item v-for="(character, index) in characters" :character="character" :key="index"></list-item>
              </select>
          </form>
          <!-- <list-item v-for="(character, index) in characters" :character="character" :key="index"></list-item> -->
      </ul>
  </div>
</template>

<script>
import ListItem from './ListItem.vue'
import { eventBus } from '../main.js'

export default {
    name:'character-list',
    data(){
        return {
            selectedCharacter: null
        }
    },
    props: ['characters'],
    components: {
        'list-item':ListItem
    },
    methods: {
        handleChange(){
            eventBus.$emit('character-select', this.selectedCharacter)
            
        }
    }
}
</script>

<style>

</style>