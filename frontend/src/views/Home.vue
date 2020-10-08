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
          @filtered="onFiltered"
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

      <!-- Modals - Separar en componentes -->
      <b-modal
        id="modal-create"
        title="Crear una tripulación"
        @hidden="cleanCrew()"
        @ok="createCrew()"
      >
        <b-form-group
          id="create-1"
          label="Nombre de tripulación"
          label-for="create-input-1"
        >
          <b-form-input id="create-input-1" v-model="crew.name" type="text" required></b-form-input>
        </b-form-group>

        <b-form-group
          id="create-2"
          label="Cantidad de tripulantes"
          label-for="create-input-2"
        >
          <b-form-input id="create-input-2"
            v-model="crew.crew_quantity"
            type="number"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="create-3"
          label="Modelo de la nave"
          label-for="create-input-3"
        >
          <b-form-input
            id="create-input-3"
            v-model="crew.ship_name"
            type="text"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="create-4"
          label="Costo de la nave"
          label-for="create-input-4"
        >
          <b-form-input id="create-input-4"
            v-model="crew.ship_cost"
            type="number"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="create-5"
          label="Velocidad máxima de la nave"
          label-for="create-input-5"
        >
          <b-form-input id="create-input-5"
            v-model="crew.ship_max_speed"
            type="number"
            required
          ></b-form-input>
        </b-form-group>

      </b-modal>

      <b-modal
        id="modal-detail"
        title="Detalles de tripulación"
        @hidden="cleanCrew()"
      >
        <b-form-group
          id="details-1"
          label="Nombre de tripulación"
          label-for="details-input-1"
        >
          <b-form-input id="details-input-1"
            v-model="crew.name" type="text" disabled></b-form-input>
        </b-form-group>

        <b-form-group
          id="details-2"
          label="Cantidad de tripulantes"
          label-for="details-input-2"
        >
          <b-form-input id="details-input-2"
            v-model="crew.crew_quantity"
            type="number"
            disabled
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="details-3"
          label="Modelo de la nave"
          label-for="details-input-3"
        >
          <b-form-input
            id="details-input-3"
            v-model="crew.ship_name"
            type="text"
            disabled
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="details-4"
          label="Costo de la nave"
          label-for="details-input-4"
        >
          <b-form-input id="details-input-4"
            v-model="crew.ship_cost"
            type="number"
            disabled
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="details-5"
          label="Velocidad máxima de la nave"
          label-for="details-input-5"
        >
          <b-form-input id="details-input-5"
            v-model="crew.ship_max_speed"
            type="number"
            disabled
          ></b-form-input>
        </b-form-group>
      </b-modal>

      <b-modal
        id="modal-edit"
        title="Editar tripulación"
        @hidden="cleanCrew()"
        @ok="updateCrew()"
      >
        <b-form-group
          id="update-1"
          label="Nombre de tripulación"
          label-for="update-input-1"
        >
          <b-form-input id="update-input-1"
            v-model="crew.name" type="text" ></b-form-input>
        </b-form-group>

        <b-form-group
          id="update-2"
          label="Cantidad de tripulantes"
          label-for="update-input-2"
        >
          <b-form-input id="update-input-2"
            v-model="crew.crew_quantity"
            type="number"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="update-3"
          label="Modelo de la nave"
          label-for="update-input-3"
        >
          <b-form-input
            id="update-input-3"
            v-model="crew.ship_name"
            type="text"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="update-4"
          label="Costo de la nave"
          label-for="update-input-4"
        >
          <b-form-input id="update-input-4"
            v-model="crew.ship_cost"
            type="number"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="update-5"
          label="Velocidad máxima de la nave"
          label-for="update-input-5"
        >
          <b-form-input id="update-input-5"
            v-model="crew.ship_max_speed"
            type="number"
          ></b-form-input>
        </b-form-group>
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
      responseMessage: '',
      crew: {
        name: null,
        crew_quantity: null,
        ship_name: null,
        ship_cost: null,
        ship_max_speed: null,
      },
      fields: ['id', 'name', 'ship_name', 'crew_quantity', 'ship_cost', 'ship_max_speed', 'detalle', 'editar', 'eliminar'],
      crews: [],
    };
  },
  computed: {
    rows() {
      return this.crews.length;
    },
  },
  mounted() {
    this.getCrews();
  },
  methods: {
    onFiltered() {
      this.currentPage = 1;
    },
    setCrew(crew) {
      this.crew = crew;
    },
    async getCrews() {
      await this.axios.get('/crews/')
        .then((response) => {
          console.log(response.data);
          this.crews = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async createCrew() {
      await this.axios.post('/crews/', this.crew)
        .then((response) => {
          console.log(response);
          this.crews.push(response.data);
          this.responseMessage = 'Tripulacion creada correctamente';
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async updateCrew() {
      await this.axios.put(`/crews/${this.crew.id}`, this.crew)
        .then((response) => {
          console.log(response);
          this.responseMessage = 'Tripulacion actualizada correctamente';
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async deleteCrew(crew) {
      await this.axios.delete(`/crews/${crew.id}`, this.crew)
        .then((response) => {
          console.log(response);
          this.crews.splice(this.crews.findIndex((actualCrew) => actualCrew.id === crew.id), 1);
          this.responseMessage = 'Tripulacion eliminada correctamente';
        })
        .catch((error) => {
          console.log(error);
        });
    },
    cleanCrew() {
      console.log('cleaning crew');
      this.crew = {
        name: null,
        crew_quantity: null,
        ship_name: null,
        ship_cost: null,
        ship_max_speed: null,
      };
    },
  },
};
</script>
