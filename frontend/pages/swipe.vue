<template>
  <b-row class="background_default">
    <b-col style="max-width: max-content;">
      <section>
      <b-card
      :title= currentUser.name
      :img-src="currentUser.image"
      img-top
      tag="article"
      style="max-width: 20rem;"
      class="mb-2"
    >
        <b-card-text>
           {{ currentUser.description }}
          <br>
          <b>{{ currentUser.city }}</b>
        </b-card-text>

        <div style="text-align: center">
        <b-button variant="primary" @click="siguiente">Siguiente</b-button>
        <font-awesome-icon :icon="['fas', 'comment']"/>
          <b-button variant="primary" @click="goProfile">Chat</b-button>
        </div>
      </b-card>
    </section>
    </b-col>
    <b-col>
      <div v-for="values in batur">
        <hr>
        <div v-for="(name, value) in values">
          <h6><b>{{ value }}</b>: {{ name}}</h6>
          <hr>
      </div>

      </div>
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
          currentUser: {
            name: "",
            image: "",
            user_id: 0,
            description: '',
            city: "",
            mail: "",
          },
          listUsers: {},
          i: 0,
          decodedStr: '',
          option: null,
          batur: [
          ]
        }
      },
      mounted() {
        this.getListUsers()
        this.getBatursUser()
      },
      methods: {
        goProfile() {
          console.log("okfjlsdf")
          console.log(this.currentUser.id)
          let items = {
            user_id: this.currentUser.id,
            chat: true
          }
          this.$router.push({
                  name: 'about',
                  params: {data: items}
                })
        },
        getListUsers() {
          const url = 'http://127.0.0.1:80/accounts'
          this.$axios.get(url)
            .then((response) => {
              console.log(response)
              if (response) {
                if (response.status === 200) {
                  this.listUsers = response.data.accounts
                  this.currentUser = this.listUsers[0]
                  console.log(this.currentUser)
                } else {
                  console.log('resposta:', response.data.data)
                }
              }
            })
            .catch((err) => {
              console.log("error")
            })
        },
        getBatursUser(id) {
          let url = 'http://127.0.0.1:80/batur/' + 0
          if (id) {
            url = 'http://127.0.0.1:80/batur/' + id
          }

          this.$axios.get(url)
            .then((response) => {
              console.log(response)
              if (response) {
                if (response.status === 200) {
                  for (let i = 0; i < response.data.baturs.length; i++) {
                    let item = {
                      "Batur": i,
                      "Disponibilidad": response.data.baturs[i].availability,
                      "Precio": response.data.baturs[i].charge,
                      "Localización": response.data.baturs[i].location,
                      "Categoria": response.data.baturs[i].subcateogry
                    }
                    this.batur.push(item)
                  }
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
        },
        siguiente() {
        this.i += 1
        this.currentUser = this.listUsers[this.i]
          this.batur = []
        this.getBatursUser(this.i)

      }

      },

    }
</script>

<style>
@import 'static/css/global.css';
</style>
