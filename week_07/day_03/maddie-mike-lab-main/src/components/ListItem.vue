<template>
  <!-- <li v-on:click="handleClick">{{character.name}}</li> -->
  <option :value="character">{{character.name}}</option>
</template>

<script>
import { eventBus } from '../main.js'

export default {
    name: 'list-item',
    props: ['character'],
    methods: {
        handleClick(){
            eventBus.$emit('character-select', this.character)
        }
    }
}
</script>

<style>

</style>