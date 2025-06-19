<template>
  <section class="sobre">
    <div class="contenido">
      <div class="texto">
        <h2>Sobre Nosotros</h2>
        <p>
          El Instituto Técnico Córdoba es una institución educativa con más de 15 años de experiencia en la formación profesional de calidad. Nuestro compromiso es brindar a nuestros estudiantes las herramientas necesarias para insertarse exitosamente en el mercado laboral.
        </p>
        <p>
          Contamos con un equipo de profesionales altamente capacitados y con amplia experiencia en sus respectivas áreas, lo que garantiza una formación integral y actualizada.
        </p>

        <div class="puntos">
          <div v-for="punto in puntos" :key="punto.texto" class="punto">
            <span class="icono">✔</span>
            {{ punto.texto }}
          </div>
        </div>

        <a href="#" class="enlace">Conoce nuestra historia →</a>
      </div>

      <div class="imagen">
        <img src="https://via.placeholder.com/400x300?text=Sobre+Nosotros" />
      </div>
    </div>
  </section>
</template>

<script setup>
const puntos = [
  { texto: '+15 años de experiencia' },
  { texto: '+5000 egresados' },
  { texto: '+20 cursos especializados' },
  { texto: 'Certificación oficial' }
]
</script>

<style scoped>
.sobre {
  background-color: #fff;
  padding: 4rem 2rem;
}
.contenido {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
  align-items: center;
}
.texto {
  flex: 1 1 500px;
}
.imagen {
  flex: 1 1 400px;
  display: flex;
  justify-content: center;
}
.imagen img {
  max-width: 100%;
}
h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
}
p {
  margin-bottom: 1rem;
}
.puntos {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem 2rem;
  margin: 2rem 0;
}
.punto {
  display: flex;
  align-items: center;
  font-weight: 500;
}
.icono {
  display: inline-block;
  background: #e3eefd;
  color: #0a58ca;
  border-radius: 999px;
  padding: 0.3rem;
  margin-right: 0.5rem;
  font-size: 0.9rem;
}
.enlace {
  color: #0a58ca;
  font-weight: bold;
  text-decoration: none;
}
.enlace:hover {
  text-decoration: underline;
}
</style>
