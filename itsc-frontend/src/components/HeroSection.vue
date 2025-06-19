<template>
  <section class="hero">
    <div class="hero-content">
      <div class="text">
        <h1>Formación Profesional de Calidad</h1>
        <p>Prepárate para el futuro con nuestros cursos especializados en tecnología, administración y oficios.</p>
        <div class="buttons">
          <button class="yellow">Ver Cursos</button>
          <button class="outline">Contáctanos</button>
        </div>
      </div>
      <img src="/hero-img.png" alt="Ilustración" class="hero-image" />
    </div>
  </section>
</template>

<style scoped>
.hero {
  background: linear-gradient(to right, #005bbb, #0078d4);
  color: white;
  padding: 4rem 2rem;
}
.hero-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: auto;
  flex-wrap: wrap;
}
.text {
  max-width: 600px;
}
h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}
p {
  margin-bottom: 2rem;
}
.buttons {
  display: flex;
  gap: 1rem;
}
button {
  padding: 0.8rem 1.2rem;
  border: none;
  font-weight: bold;
  border-radius: 5px;
  cursor: pointer;
}
.yellow {
  background-color: #fdd835;
  color: #000;
}
.outline {
  background-color: transparent;
  border: 2px solid white;
  color: white;
}
.hero-image {
  max-width: 400px;
  margin-top: 2rem;
}
</style>
