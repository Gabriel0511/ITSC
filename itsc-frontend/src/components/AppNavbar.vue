<template>
  <nav class="navbar">
    <div class="logo">
      <img src="/logo.svg" alt="ITSC Logo" />
      <div class="title">
        <strong>Instituto Técnico Córdoba</strong>
        <small>Formación Profesional de Calidad</small>
      </div>
    </div>
    <ul class="nav-links">
      <li><a href="#">Inicio</a></li>
      <li><a href="#">Cursos</a></li>
      <li><a href="#">Nosotros</a></li>
      <li><a href="#">Instalaciones</a></li>
      <li><a href="#">Contacto</a></li>
      <li><a class="button" href="#">Inscríbete</a></li>
    </ul>
  </nav>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
}
.logo {
  display: flex;
  align-items: center;
}
.logo img {
  height: 40px;
  margin-right: 10px;
}
.title {
  display: flex;
  flex-direction: column;
  line-height: 1.2;
}
.nav-links {
  display: flex;
  list-style: none;
  gap: 1rem;
  align-items: center;
}
.nav-links a {
  text-decoration: none;
  color: #1e293b;
  font-weight: 500;
}
.button {
  background-color: #0a58ca;
  color: white;
  padding: 0.4rem 0.8rem;
  border-radius: 5px;
}
</style>
