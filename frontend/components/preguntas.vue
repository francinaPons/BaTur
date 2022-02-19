<template>
<div>
  <b-button variant="primary" @click="ofrecer1">
    QUIERO OFRECER UN BATUR
  </b-button>
  <b-button variant="primary" @click="ofrecer1">
    QUIERO BUSCAR UN BATUR
  </b-button>
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
      const url = 'http://127.0.0.1:80/login'
      //this.ofrecer = true;
      this.$emit('initialComponent', false)
      //this.initialComponent = false;
    },

  }
}
</script>
