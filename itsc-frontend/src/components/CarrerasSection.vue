<template>
  <section class="carreras">
    <h2>Nuestras Carreras</h2>
    <p class="desc">
      Conocé nuestras propuestas académicas en tecnología, administración y oficios.
    </p>
    <div class="grid">
      <div class="card" v-for="carrera in carreras" :key="carrera.nombre">
        <img :src="carrera.img" alt="Imagen de carrera" class="card-img" />
        <h3>{{ carrera.nombre }}</h3>
        <p>{{ carrera.descripcion }}</p>
        <button>Ver más</button>
      </div>
    </div>
  </section>
</template>

<script setup>
const carreras = [
  {
    nombre: 'Desarrollo Web',
    descripcion: 'Aprendé a crear sitios y aplicaciones modernas usando tecnologías actuales.',
    img: 'https://via.placeholder.com/400x200?text=Desarrollo+Web'
  },
  {
    nombre: 'Administración de Empresas',
    descripcion: 'Formate en gestión administrativa, contable y recursos humanos.',
    img: 'https://via.placeholder.com/400x200?text=Administración'
  },
  {
    nombre: 'Electricidad Industrial',
    descripcion: 'Capacitación en instalaciones eléctricas y mantenimiento industrial.',
    img: 'https://via.placeholder.com/400x200?text=Electricidad'
  },
  {
    nombre: 'Redes y Telecomunicaciones',
    descripcion: 'Configuración y mantenimiento de redes informáticas y telecomunicaciones.',
    img: 'https://via.placeholder.com/400x200?text=Redes'
  }
]
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
