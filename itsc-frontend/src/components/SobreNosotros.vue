<template>

  <section class="hero">
    <div class="hero-content">
      <div class="text">
        <h1>Sobre Nosotros</h1>
        <p>El Instituto Técnico Superior Córdoba es una institución educativa con más de 10 años de experiencia en la formación profesional de calidad. Nuestro compromiso es brindar a nuestros estudiantes las herramientas necesarias para insertarse exitosamente en el mercado laboral.
        </p>
         <p>
          Contamos con un equipo de profesionales altamente capacitados y con amplia experiencia en sus respectivas áreas, lo que garantiza una formación integral y actualizada.
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>

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
.hero {
  background: linear-gradient(to right, #005bbb, #0078d4);
  color: white;
  padding: 2rem 2rem;
}
.hero-content {
  display: flex;
  justify-content: center;
  align-items: center;
  max-width: 1200px;
  margin: auto;
  flex-wrap: wrap;
}
.text {
  max-width: 100%;
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
