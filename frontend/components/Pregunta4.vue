<template>
  <div>
    <h3>4/4</h3>
    <h1>¿Qué tipo de actividad propones?</h1>
    <h1>Zer jarduera mota proposatzen duzu?</h1>

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

<script>
export default {
  name: "Pregunta4",
  data() {
      return {
        selected: [], // Must be an array reference!
        options: [
          { text: 'Gastronomia', value: 'Interés Gastronómico' },
          { text: 'Playas', value: 'Playas' },
          { text: 'Interés cultural', value: 'De interés cultural' },
          { text: 'Monumentos históricos', value: 'Monumentos históricos' },
          { text: 'Discotecas', value: 'Discotecas' },
        ]
      }
    },
  methods:{
      check(){
        this.$emit('respuestaPregunta4', this.selected[0])
        console.log(this.selected)
      }
  }
}
</script>

<style>

</style>
