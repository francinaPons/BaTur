<!-- Please remove this file from your project -->
<template>
  <section class="section login">
    <div class="container">
      <div class="columns">
        <div class="column is-4 is-offset-4">
          <div id="imagesMarcaId" style="margin-top:27px;margin-bottom:50px">
            <b-img id="marcaImageId" src="~/static/batur.png" />
          </div>

          <Notification v-if="error" :message="error" />

          <b-form-group
            id="username"
            label="Usuario"
            label-for="username"
            label-cols-md="4"
            label-size="md"
            size="md"
            class="mb-4"
          >
            <b-form-input id="username" v-model="username" size="md" />
          </b-form-group>

          <b-form-group
            id="password"
            label="Contraseña"
            label-for="password"
            label-cols-md="4"
            label-size="md"
            size="md"
            class="mb-4"
          >
            <b-form-input id="password" v-model="password" type="password" size="md" />
          </b-form-group>

          <b-button variant="primary" @click="login">
            LOGIN
          </b-button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'NuxtTutorial',
  data: function () {
    return {
      username: "",
      password: "",
      error: false,
    }
  },
  methods: {
    login() {
      const url = 'http://127.0.0.1:80/login'
      const params = {
        username: this.username,
        password: this.password,
      }
      this.$axios.post(url, params)
          .then((response) => {
            console.log(response)
            if (response) {
              if (response.status === 200) {
                this.$router.push('/about')
              } else {
                console.log('resposta:', response.data.data)
              }
            }
          })
      .catch((err) => {
        this.$router.push('/')
        this.error = "error al iniciar sesion";
      })
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
