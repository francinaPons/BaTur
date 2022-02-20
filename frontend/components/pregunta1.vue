<template>
<div>
  <h3>1/4</h3>
  <h1>¿Quieres cobrar tu Batur?</h1>
  <h1>Zure Batur-a kobratu nahi duzu?</h1>

  <div>
    <b-form-checkbox-group
        @change="check()"
        id="checkbox-group-1"
        v-model="selected"
        :options="options"
        name="flavour-1"
        stacked
      ></b-form-checkbox-group>
  </div>



  </div>

</template>

<style>

</style>
<script>
export default {

    data() {
      return {
        selected: [], // Must be an array reference!
        options: [
          { text: 'No/Ez', value: 'no' },
          { text: 'Acepto propinas/Eskupekoak ba', value: 'propina' },
          { text: 'A partir de 10', value: '10' },
          { text: 'A partir de 20', value: '20' },
          { text: 'A partir de 40', value: '40' },
          { text: 'A partir de 100 €', value: '100' },
        ]
      }
    },
  methods:{
      check(){
        this.$emit('respuestaPregunta1', this.selected)
        console.log(this.selected)
      }
  }
  }

</script>
