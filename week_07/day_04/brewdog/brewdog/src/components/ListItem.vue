<template>
  <option :value="beer">{{beer.name}}</option>
</template>

<script>
import { eventBus } from '../main.js'


export default {
    name: 'list-item',
    props: ['beer'],
    methods: {
        handleClick(){
            eventBus.$emit('beer-select', this.beer)
        }
    }
}
</script>

<style>

</style>