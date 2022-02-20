<template>
<div>
  <h3>3/4</h3>
  <h1>¿Cúal es tu disponibilidad?</h1>
  <h1>Zein da zure disponibilitatea?</h1>

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

    data() {
      return {
        selected: [], // Must be an array reference!
        options: [
          { text: 'Estoy siempre disponible/Beti nago prest', value: 'DISPONIBLE' },
          { text: 'Fines de semana/Aste bukaeretan', value: 'FINDESEMANA' },
          { text: 'Entre semana/Astean zehar', value: 'ENTRESEMANA' },
          { text: 'Preguntar por chat/Galdeti', value: 'PREGUNTAR' },

        ]
      }
    },
  methods:{
      check(){
        this.$emit('respuestaPregunta3', this.selected[0])
        console.log(this.selected)
      }
  }
  }

</script>

<style scoped>

</style>
