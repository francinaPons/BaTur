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

        <b-button href="/baturs" variant="primary">Ver mis BaTurs</b-button>
        <b-button variant="primary">Ajustes</b-button>
        <b-button variant="primary">Mis chats</b-button>
      </b-card>
    </section>
    </b-col>
    <b-col>
      hola
    </b-col>
    </b-row>

</template>

<script>
    export default {
      name: "Profile",
      data: function () {
        return {
          name: "",
          image: "",
          user_id: 0,
          description: "",
          city: "",
          mail: "",
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

      }
    }
</script>

<style>

</style>
