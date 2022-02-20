<template>
<div class="div-1">
  <div style="margin: 20px;">
    <div style="padding-bottom: 30px;">
      <h3>¡Hola!</h3>
      <h3>¿Qué quieres hacer?</h3>
    </div>


  <b-button variant="primary" @click="ofrecer1" style="height: 100px; font-size: 25px; font-weight: bold">
    QUIERO OFRECER UN BATUR
  </b-button>
    </div>
  <div>
  <b-button variant="primary" @click="ofrecer2" style="height: 100px; font-size: 25px; font-weight: bold">
    QUIERO BUSCAR UN BATUR
  </b-button>
    </div>
  </div>

</template>


<script>
import NuxtLogo from "~/components/NuxtLogo";
import Preguntas from "~/components/preguntas";
export default {
  name: 'NuxtTutorial',
  components: {Preguntas, NuxtLogo},
  data: function () {
    return {
      initialComponent: true,
      ofrecer: false,
      reservar: false
    }
  },
  methods: {
    ofrecer1() {
      this.$emit('initialComponent', false)
    },
    ofrecer2() {
      this.$router.push('/swipe')
    },

  }
}
</script>
