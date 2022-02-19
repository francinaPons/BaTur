<template>
  <section class="background_default">
    <b-card
    :title= username
    img-src="~/static/aitor_surfer.jpeg"
    img-top
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-text>
      Some quick example text to build on the card title and make up the bulk of the card's content.
    </b-card-text>

    <b-button href="/baturs" variant="primary">Ver mis BaTurs</b-button>
    <b-button variant="primary">Ajustes</b-button>
     <b-button variant="primary">Mis chats</b-button>
     <b-img id="marcaImageId" src="~/static/batur.png" />
  </b-card>

  </section>
</template>

<script>
    export default {
        name: "Profile",
        data: function () {
          return {
            username: "",
            icon: "",
          }
        },
    }
</script>

<style scoped>

</style>
