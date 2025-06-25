<template>
  <section class="carreras">
    <h2>Nuestras Carreras</h2>
    <p class="desc">
      Conocé nuestras propuestas académicas en tecnología, administración y oficios.
    </p>
    <div class="grid">
      <div class="card" v-for="carrera in carreras" :key="carrera.id">
        <img :src="carrera.img" alt="Imagen de carrera" class="card-img" />
        <h3>{{ carrera.nombre }}</h3>
        <p>{{ carrera.descripcion }}</p>
        <button>Ver más</button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const carreras = ref([])

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/carreras/')
    carreras.value = response.data
  } catch (error) {
    console.error('Error al cargar las carreras:', error)
  }
})
</script>

<style scoped>
.carreras {
  padding: 4rem 2rem;
  background-color: #ffffff;
  text-align: center;
}
.desc {
  max-width: 600px;
  margin: 0 auto 2rem;
}
.grid {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
}
.card {
  background: #f9fafb;
  border-radius: 12px;
  width: 280px;
  padding: 1rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  text-align: left;
  display: flex;
  flex-direction: column;
}
.card-img {
  width: 100%;
  border-radius: 8px;
  margin-bottom: 1rem;
}
h3 {
  margin: 0.5rem 0;
}
button {
  margin-top: auto;
  align-self: flex-start;
  background-color: #0a58ca;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: bold;
}
button:hover {
  background-color: #084298;
}
</style>
