<template>
  <div class="home mt-5">

    <b-container class="bv-example-row">

      <b-row>
        <b-col>
          <h1>Tripulantes</h1>
        </b-col>

        <b-col>
          <b-form-input
            v-model="filter"
            type="search"
            id="filterInput"
            placeholder="Buscar..."
          ></b-form-input>
        </b-col>

        <b-col>
          <b-button
            variant="success"
            v-b-modal.modal-create
          >
            Agregar tripulación
          </b-button>
        </b-col>

      </b-row>

      <!-- Crew Table -->
      <b-row>
        <b-table
          :items="crews"
          :current-page="currentPage"
          :filter="filter"
          :per-page="perPage"
          :fields="fields"
          striped
          hover
        >
          <template v-slot:cell(detalle)="row">
            <b-button
              size="sm"
              class="mr-2"
              variant="success"
              @click="setCrew(row.item)"
              v-b-modal.modal-detail
            >
              Detalle
            </b-button>
          </template>

          <template v-slot:cell(editar)="row">
            <b-button
              size="sm"
              class="mr-2"
              variant="success"
              @click="setCrew(row.item)"
              v-b-modal.modal-edit
            >
              Editar
            </b-button>
          </template>

          <template v-slot:cell(eliminar)="row">
            <b-button
              size="sm"
              class="mr-2"
              variant="danger"
              @click="deleteCrew(row.item)"
            >
              Eliminar
            </b-button>
          </template>

        </b-table>

        <b-pagination
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="my-table"
        ></b-pagination>

      </b-row>

      <!-- Modals -->
      <b-modal
        id="modal-create"
        title="Crear una tripulación"
        @hidden="cleanCrew()"
        @ok="createCrew()"
      >
        <p class="my-4">Hello from create!</p>
      </b-modal>

      <b-modal
        id="modal-detail"
        title="Detalles de tripulación"
        @hidden="cleanCrew()"
      >
        <p class="my-4">Hello from details!</p>
      </b-modal>

      <b-modal
        id="modal-edit"
        title="Editar tripulación"
        @hidden="cleanCrew()"
        @ok="updateCrew()"
      >
        <p class="my-4">Hello from edit!</p>
      </b-modal>

    </b-container>
  </div>
</template>

<script>

export default {
  name: 'Home',
  components: {
  },
  data() {
    return {
      perPage: 6,
      currentPage: 1,
      filter: null,
      crew: null,
      fields: ['age', 'first_name', 'detalle', 'editar', 'eliminar'],
      crews: [
        { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
        { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
        { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
        { age: 38, first_name: 'Jami', last_name: 'Carney' },
        { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
        { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
        { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
        { age: 38, first_name: 'Jami', last_name: 'Carney' },
        { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
        { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
        { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
        { age: 38, first_name: 'Jami', last_name: 'Carney' },
        { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
        { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
        { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
        { age: 38, first_name: 'Jami', last_name: 'Carney' },
      ],
    };
  },
  computed: {
    rows() {
      return this.crews.length;
    },
  },
  methods: {
    setCrew(crew) {
      console.log(crew.age);
    },
    createCrew() {
      console.log('creating');
    },
    detailCrew(crew) {
      console.log(crew.age);
    },
    updateCrew(crew) {
      console.log(crew.age);
    },
    deleteCrew(crew) {
      console.log(crew.age);
    },
    cleanCrew() {
      console.log('cleaning crew');
      this.crew = null;
    },
  },
};
</script>
