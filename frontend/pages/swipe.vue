<template>
  <b-row class="background_default">
    <b-col style="max-width: max-content;">
      <section>
      <b-card
      :title= name
      img-src="~/static/aitor_surfer.jpeg"
      img-top
      tag="article"
      style="max-width: 20rem;"
      class="mb-2"
    >
        <b-card-text>
           {{ description }}
          <br>
          <b>{{ city }}</b>
        </b-card-text>

        <!--<b-button href="/baturs" variant="primary">Ver mis BaTurs</b-button> -->
        <div style="text-align: center">
        <b-button variant="primary" >Siguiente</b-button>
        <b-button variant="primary" >Chat</b-button>
        </div>
      </b-card>
    </section>
    </b-col>
    <b-col>
     HOLA
    </b-col>
    </b-row>

</template>

<script>
import Baturs from "~/pages/baturs";
    export default {
      name: "Profile",
      components: {Baturs},
      data: function () {
        return {
          name: "",
          image: "",
          user_id: 0,
          description: "",
          city: "",
          mail: "",
          option: null,

        }
      },
      mounted() {
        this.getProfile()
      },
      methods: {
        getProfile() {

          const url = 'http://127.0.0.1:80/accountId/0'
          this.$axios.get(url)
            .then((response) => {
              console.log(response)
              if (response) {
                if (response.status === 200) {
                  // TODO: omplir info de l'usuari
                  this.name = response.data.account.name
                  this.description = response.data.account.description
                  this.city = response.data.account.city
                  console.log(this.name)

                } else {
                  console.log('resposta:', response.data.data)
                }
              }
            })
            .catch((err) => {
              console.log("error")
            })
        },
        select_options(option){
          this.option = option;
        }

      }
    }
</script>

<style>
@import 'static/css/global.css';
</style>
