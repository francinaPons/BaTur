<template>
<div>
  <b-button variant="primary" @click="ofrecer1">
    QUIERO OFRECER UN BATUR
  </b-button>
  <b-button variant="primary" @click="ofrecer2">
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
      this.$emit('initialComponent', false)
    },
    ofrecer2() {
      this.$router.push('/swipe')
    },


  }
}
</script>
