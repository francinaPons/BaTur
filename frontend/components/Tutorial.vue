<!-- Please remove this file from your project -->
<template>
  <div>
    <b-button @click="getActivities"></b-button>
  </div>
</template>

<script>
export default {
  name: 'NuxtTutorial',
  methods: {
    getActivities() {
      console.log("Jaskdljf")
      const url = 'http://127.0.0.1:80/activity/1'
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
