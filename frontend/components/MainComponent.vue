<!-- Please remove this file from your project -->
<template>
  <div>
     <b-button style="float: right" @click="goProfile">
      PERFIL
    </b-button>

  <section class="section login">
    <h1 style="text-align: center">BATUR</h1>
    <div class="container">


      <div class="columns">
        <div class="column is-4 is-offset-4">

          <preguntas v-if="initialComponent" @initialComponent="onClickChild"></preguntas>

          <pregunta1 v-if="!initialComponent && respuestaPregunta1===null" @respuestaPregunta1="onClickPregunta1"></pregunta1>

          <pregunta2 v-if="respuestaPregunta1!==null && respuestaPregunta2city === null"
                     @respuestaPregunta2city="onClickPregunta2city"
                     @respuestaPregunta2text="onClickPregunta2text"
                     >
          </pregunta2>

          <Pregunta3 v-if="respuestaPregunta2city!==null && respuestaPregunta3===null"
          @respuestaPregunta3="onClickPregunta3"> </Pregunta3>


          <Pregunta4 v-if="respuestaPregunta3!==null && respuestaPregunta4===null"
          @respuestaPregunta4="onClickPregunta4"> </Pregunta4>

          <div v-if="respuestaPregunta4!==null"   >
            <h4>Precio: {{respuestaPregunta1}}</h4>
            <h4>Ciudad: {{respuestaPregunta2city}}</h4>
            <h4>Descripción: {{respuestaPregunta2text}}</h4>
            <h4>Disponibilidad: {{respuestaPregunta3}}</h4>
            <h4>Actividad: {{respuestaPregunta4}}</h4>

            <b-button @click="terminarBatur">
              Terminar
            </b-button>

          </div>






        </div>
      </div>

    </div>
  </section>
  </div>
</template>


<style>
</style>
<script>
import NuxtLogo from "./NuxtLogo";
import Preguntas from "./preguntas";
export default {
  name: 'NuxtTutorial',
  components: {Preguntas, NuxtLogo},
  data: function () {
    return {
      username: "",
      password: "",
      error: false,
      ofrecer: false,
      reservar: false,
      initialComponent: true,
      respuestaPregunta1: null,
      respuestaPregunta2city: null,
      respuestaPregunta2text: null,
      respuestaPregunta3: null,
      respuestaPregunta4: null,

    }
  },
  methods: {
    onClickChild (value) {
          this.initialComponent = value;
          console.log(value) // someValue
      },
    onClickPregunta1(value){
      this.respuestaPregunta1 = value;
    },
    onClickPregunta2city(value){
      this.respuestaPregunta2city = value;
    },
    onClickPregunta2text(value){
      this.respuestaPregunta2text = value;
    },
    onClickPregunta3(value){
      this.respuestaPregunta3 = value;
    },
    onClickPregunta4(value){
      this.respuestaPregunta4 = value;
    },
    ofrecer1() {
      const url = 'http://127.0.0.1:80/login'
      this.ofrecer = true;
      this.initialComponent = false;
    },
    buscar() {
      const url = 'http://127.0.0.1:80/login'

      this.initialComponent = false;
    },
    terminarBatur(){
      //TODO: AFEGIR TOTES LES VARS A BBDD
      this.$router.push('/about')
    },
    goProfile(){
      this.$router.push('/about')
    },
    getActivities() {
      console.log("Jaskdljf")
      const url = 'http://127.0.0.1:80/activity/10'
      this.$axios.get(url)
          .then((response) => {
            if (response) {
              console.log('response: ')
            }
      })
      this.$router.push('/about')
    }
  }
}
</script>
<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}

.login {
    background-color: #dce5cf !important;
}

.b-toaster.b-toaster-top-center {
    top: 15rem;
}
.toast-body {
    padding: 1rem !important;;
    text-align: center !important;
}
.toast {
    max-width: 400px !important;
    width: 400px !important;
}

</style>
