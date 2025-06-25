<template>
  <nav class="navbar">
    <div class="logo">
      <img src="/itsc-logo.jpg" alt="ITSC Logo" />
      <div class="title">
        <strong>Instituto Técnico Superior Córdoba</strong>
        <small>Ministerio de Educación</small>
        <small>Dirección General de Educación Técnica y Formación Profesional</small>
        <small>Subdirección de Educación Superior</small>
      </div>
    </div>
    <ul class="nav-links">
      <li><a href="#">Inicio</a></li>
      <li><a href="#">Sobre Nosotros</a></li>
      <li><a href="#">Sede Central</a></li>
      <li><a href="#">Carreras</a></li>
      <li><a href="#">Novedades</a></li>
      <li><a href="#">Otras Sedes</a></li>
      <li><a href="#">Contacto</a></li>
      <li><a class="button" target="_blank" href="https://8048bf14c1.clvaw-cdnwnd.com/f80d7a5356be0d319861778d7e89b608/200002897-3efae3efb0/REQUISITOS%20matriculacion.pdf">Requisitos Inscripción</a></li>
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
