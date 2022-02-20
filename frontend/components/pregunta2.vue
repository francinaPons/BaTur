<template>
  <div>
    <h3>2/4</h3>
    <h6>¿Donde selocaliza tu Batur?/Non kokatzen da zure Batur-a?</h6>

    <b-form-select v-model="selected" :options="options" size="sm" @change="getCityId"></b-form-select>
    <div>
      <h6>¿Qué punto de interés quieres visitar?/Zer nahi duzu bisitatu?</h6>
    <b-form-select v-model="selected2" v-if="selected" :options="options2" size="sm" ></b-form-select>

    </div>

    <h1>Describe brevemente tu Bitur/Deskribatu labur-labur zure Bitur-a</h1>
    <div class="form-group">

        <b-form-textarea
          id="textarea"
          v-model="review"
          :state="review.length<=250 && review.length>=10"
          placeholder="Enter something..."
          rows="3"
          max-rows="6"
        ></b-form-textarea>
    </div>

    <b-button variant="primary" @click="siguiente">
    Siguiente
  </b-button>
  </div>

</template>

<script>
export default {
  name: "pregunta2",

  data: function () {
    return {
      review: "",
      selected: null,
      options: [
        { value: null, text: 'Selecciona una ciudad' }
      ],
      selected2: null,
      options2: [

      ]
    }
  },
  mounted() {
    const url = 'http://127.0.0.1:80/cities'
    this.$axios.get(url)
        .then((response) => {
          console.log(response)
          if (response) {
            if (response.status === 200) {
              for (let i = 0; i < response.data.length; i++) {
                // console.log(response.data[i])
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
  methods: {
    siguiente(){
      if(this.selected !== null && this.review.length <= 250 ){

        this.$emit('respuestaPregunta2city', this.selected2)
        this.$emit('respuestaPregunta2text', this.review)

      }
      //TODO ELSE POP UP NO SELECTED OR TEXT NOT LENGHT

      //Todo: si city y texto -> emit
      },
    getPOIs(id){
       const url = 'http://127.0.0.1:80/POISCITY/' + id
    this.$axios.get(url)
        .then((response) => {
          console.log(response)
          if (response) {
            if (response.status === 200) {
              this.options2 = []
              for (let i= 0; i < response.data.length; i++) {
                this.options2.push(response.data[i].name)
              }
              console.log(response)
            } else {
              console.log('resposta:', response.data.data)
            }
          }
        })
    .catch((err) => {
      console.log("error")
    })
    },
      getCityId() {

      const url = 'http://127.0.0.1:80/city/' + this.selected
    this.$axios.get(url)
        .then((response) => {
          console.log(response)
          if (response) {
            if (response.status === 200) {
              console.log(response.data[0].city_id)
              this.getPOIs(response.data[0].city_id)
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
  .custom_select {
    width: 80rem;
  }

</style>
