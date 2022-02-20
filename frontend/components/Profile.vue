<template>
  <div>
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
        <b-button variant="primary" @click="select_options('batur')">Mis Baturs</b-button>
        <b-button variant="primary" @click="select_options('ajustes')">Ajustes</b-button>
        <b-button variant="primary" @click="select_options('chat')">Mis chats</b-button>
        <b-button variant="primary" @click="logout">Logout</b-button>
      </b-card>
    </section>
    </b-col>
    <b-col>
      <Baturs v-if="option === 'batur'" ></Baturs>
      <Ajustes v-if="option === 'ajustes'" :id_user="id_user" :username="username"></Ajustes>
      <Chat v-if="option==='chat'"></Chat>
    </b-col>
    </b-row>

    </div>

</template>

<script>
    import Baturs from "~/pages/baturs";
    export default {
      name: "Profile",
      components: {Baturs},
      data: function () {
        return {
          name: "",
          id_user: null,
          image: "",
          user_id: 0,
          description: "",
          city: "",
          mail: "",
          option: null,
          username:""

        }
      },
      mounted() {
        if (this.$route.params['data'].user_id){
          this.id_user = this.$route.params['data'].user_id
          this.option = 'chat'
        }
        else {
          this.id_user = this.$route.params['data'];
        }
        this.getProfile()
      },
      methods: {
        logout() {
          this.$router.push('/')
        },
        getProfile() {
          console.log(this.id_user)
          const url = 'http://127.0.0.1:80/accountId/' + this.id_user;
          this.$axios.get(url)
            .then((response) => {
              console.log(response)
              if (response) {
                if (response.status === 200) {
                  // TODO: omplir info de l'usuari
                  this.name = response.data.account.name
                  this.description = response.data.account.description
                  this.city = response.data.account.city
                  this.username = response.data.account.username
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

</style>
