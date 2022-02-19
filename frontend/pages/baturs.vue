<template>
  <div>
    <h1>Mis Betours</h1>
    <div class="container">
      <b-table
      id="users-list-table"
      show-empty
      :items="filtered"
      :per-page="perPage"
      :current-page="currentPage"
      :fields="fields"
      outlined="outlined"
      head-variant="light"
      :hover="hover"
      class="text-left"
      :sort-by.sync="sortBy"
      :sort-desc.sync="sortDesc"
      sort-icon-left
      empty-text="No se han encontrado registros"
    >
      <template v-slot:head(id)="data">
        <b-input-group>
          <span style="margin-top:5px">{{ data.label }}</span>
          <b-form-input
            id="searchidinputid"
            v-model="filters['id']"
            size="sm"
            style="color:rgb(37, 125, 226);border:0;margin-left:10px;text-align:center"
            class="noactivesearch"
            @input="requireElement('searchidinputid')"
          />
        </b-input-group>
      </template>
      <template v-slot:head(createdat)="data">
        <b-input-group>
          <span style="margin-top:5px">{{ data.label }}</span>
          <b-form-input
            id="searchcreatedatinputid"
            v-model="filters['created_at']"
            size="sm"
            style="color:rgb(37, 125, 226);border:0;margin-left:10px;text-align:center"
            class="noactivesearch"
            @input="requireElement('searchcreatedatinputid')"
          />
        </b-input-group>
      </template>
      <template v-slot:head(username)="data">
        <b-input-group>
          <span style="margin-top:5px">{{ data.label }}</span>
          <b-form-input
            id="searchusernameinputid"
            v-model="filters['username']"
            size="sm"
            style="color:rgb(37, 125, 226);border:0;margin-left:10px;text-align:center"
            class="noactivesearch"
            @input="requireElement('searchusernameinputid')"
          />
        </b-input-group>
      </template>
      <template v-slot:head(profile.Value)="data">
        <b-input-group>
          <span style="margin-top:5px">{{ data.label }}</span>
          <b-form-input
            id="searchprofileidinputid"
            v-model="filters['profile.Value']"
            size="sm"
            style="color:rgb(37, 125, 226);border:0;margin-left:10px;text-align:center"
            class="noactivesearch"
            @input="requireElement('searchprofileidinputid')"
          />
        </b-input-group>
      </template>
      <template v-slot:head(email)="data">
        <b-input-group>
          <span style="margin-top:5px">{{ data.label }}</span>
          <b-form-input
            id="searchemailinputid"
            v-model="filters['email']"
            size="sm"
            style="color:rgb(37, 125, 226);border:0;margin-left:10px;text-align:center"
            class="noactivesearch"
            @input="requireElement('searchemailinputid')"
          />

        </b-input-group>
      </template>
      <template v-slot:cell(buttonedit)="data">
        <b-row style="width:100%">
          <b-button id="show-btn" v-b-toggle.sidebar-right style="font-size: 0.85em;height:26px;line-height: 9px;width:100%" variant="primary" @click="sideModal(data.item.id)">
            Detalles
          </b-button>
        </b-row>
      </template>
    </b-table>
    </div>
  </div>
</template>

<script>
    export default {
        name: "baturs",
      data: function () {
        return {
          modalclass: ['modalclass'],
          userdetail: {
          id: 0,
          withprops: false
      },
      isBusy: false,
      perPage: 10,
      currentPage: 1,
      items: this.getBarturs(),
      fields: [
        { key: 'id', label: 'id', sortable: true },
        { key: 'charge', label: "Precio", sortable: true},
        { key: 'location', label: "Localización", sortable: true },
        { key: 'description', label: "description", sortable: true }],
      hover: true,
      filters: {
        id: '', created_at: '', username: '', 'profile.Value': '', email: '', uid: ''
      },
      sortBy: 'id',
      sortDesc: false,
      pagesgroups: [5, 10, 15, 20, 25, 50]
        }
      },
      rows () {
      if (this.items === undefined) {
        return 0
      } else {
        return this.filtered.length
        // return this.items.length
      }
    },
    filtered () {
      if (this.items !== undefined && this.items.length > 0) {
        console.log(this.items)
        const filtered = this.items.filter((item) => {
          const subfilters = {}
          subfilters.id = true
          subfilters.precio = true
          subfilters.localizacion = true
          subfilters.descripcion = true

          // return this.$t(item.profile.Value).toLowerCase().includes(String(this.filters['profile.Value']).
          // toLowerCase()) && Object.keys(subfilters).every(key => String(item[key]).toLowerCase().
          // includes(this.filters[key].toLowerCase()))
          return Object.keys(this.filters).every(key =>
            String(item[key]).toLowerCase().includes(this.filters[key].toLowerCase()))
        })
        return filtered.length > 0 ? filtered : []
      } else {
        return this.items
      }
    },
      computed: {
          rows () {
      if (this.items === undefined) {
        return 0
      } else {
        return this.filtered.length
        // return this.items.length
      }
    },
    filtered () {
      if (this.items !== undefined && this.items.length > 0) {
        console.log(this.items)
        const filtered = this.items.filter((item) => {
          const subfilters = {}
          subfilters.id = true
          subfilters.username = true
          subfilters.email = true
          // return this.$t(item.profile.Value).toLowerCase().includes(String(this.filters['profile.Value']).toLowerCase()) && Object.keys(subfilters).every(key => String(item[key]).toLowerCase().includes(this.filters[key].toLowerCase()))
          return Object.keys(this.filters).every(key =>
            String(item[key]).toLowerCase().includes(this.filters[key].toLowerCase()))
        })
        return filtered.length > 0 ? filtered : []
      } else {
        return this.items
      }
    },
      },

    methods: {
      getBarturs() {
        const url = 'http://127.0.0.1:80/batur/1'
        this.$axios.get(url)
            .then((response) => {
              console.log(response)
              if (response) {
                if (response.status === 200) {
                  this.items = response.data.baturs;
                  console.log(this.items)


                  console.log("baturssss")
                } else {
                  console.log('resposta:', response.data.data)
                }
              }
            })
        .catch((err) => {
          console.log("error")
        })
        }

     },
    }
</script>

<style>
@import 'static/css/global.css';
  .container {
    min-height: 0;
  }
</style>
