<template>
  <div>
    <b-container fluid>
      <b-row class="my-1">
        <b-col sm="3">
          <label>Nombre:</label>
        </b-col>
        <b-col sm="9">
          <b-form-input v-model="name" type="text"></b-form-input>
        </b-col>
      </b-row>


      <b-row class="my-1">
        <b-col sm="3">
          <label>Descripción:</label>
        </b-col>
        <b-col sm="9">
          <b-form-input v-model="description" type="text"></b-form-input>
        </b-col>
      </b-row>



      <b-row class="my-1">
        <b-col sm="3">
          <label>Ciudad:</label>
        </b-col>
        <b-col sm="9">
          <b-form-select v-model="selected" :options="options" size="sm" ></b-form-select>
        </b-col>
      </b-row>
    <b-button @click="submit">
      SUBMIT
    </b-button>
    </b-container>
  </div>
</template>

<script>
  export default {
    props: ['id_user', 'username'],
    data() {
      return {
        id_user: this.id_user,
        username: this.username,
        name: "",
        description: "",
        city: "",
        options: [
          { value: null, text: 'Selecciona una ciudad' }
        ],
        selected: null,
        userDetailsMap: {}

      }
    },
    mounted() {
      console.log(this.id_user)

      const url = 'http://127.0.0.1:80/cities'
      this.$axios.get(url)
          .then((response) => {
            console.log(response)
            if (response) {
              if (response.status === 200) {
                for (let i = 0; i < response.data.length; i++) {
                  this.options.push(response.data[i].city_name)
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
    methods:{
      submit() {
        const url = 'http://127.0.0.1:80/account/' + this.username
        const params = {
          name: this.name,
          city: this.city,
          description: this.description
        }
        this.$axios.post(url, params)
          .then((response) => {
            if (response) {
              if (response.status === 200) {
                console.log("S'ha guardat correctament")
                this.city = ""
                this.options = [
                  { value: null, text: 'Selecciona una ciudad' }
                ]
                this.name = ""
                this.description = ""
              } else {
                console.log('resposta:', response.data.data)
              }
            }
          })
          .catch((err) => {
            console.log("error")
          })

      }
    }
  }
</script>

<style>
   @import 'static/css/global.css';

</style>
