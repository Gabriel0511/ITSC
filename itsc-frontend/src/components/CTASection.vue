<template>
  <section class="cta">
    <div class="cta-content">
      <div>
        <h2>¿Listo para dar el siguiente paso en tu carrera?</h2>
        <p>Inscríbete ahora y comienza tu formación profesional con nosotros.</p>
      </div>
      <a href="#contacto" class="cta-btn">Inscríbete Ahora</a>
    </div>
  </section>
</template>

<style scoped>
.cta {
  background-color: #0056b3;
  color: white;
  padding: 3rem 2rem;
}
.cta-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}
h2 {
  font-size: 1.8rem;
  margin-bottom: 0.5rem;
}
p {
  margin: 0;
}
.cta-btn {
  background-color: white;
  color: #0056b3;
  padding: 0.75rem 1.5rem;
  border-radius: 6px;
  text-decoration: none;
  font-weight: bold;
  transition: background 0.2s;
}
.cta-btn:hover {
  background-color: #e3eefd;
}
</style>
