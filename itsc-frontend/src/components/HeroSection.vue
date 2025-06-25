<template>
  <section class="hero">
    <div class="hero-content">
    </div>
  </section>
  <section class="mapa">

    <h3>Sede Central Rio Negro 77</h3>
  <div class="mapa-grid">

    <div class="mapa-contenedor">
      <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3405.1229042784757!2d-64.20854912337852!3d-31.41073969598007!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94329884bf190281%3A0x33bf190637c92a0f!2sInstituto%20T%C3%A9cnico%20Superior%20C%C3%B3rdoba!5e0!3m2!1ses-419!2sar!4v1750876437947!5m2!1ses-419!2sar" width="600" height="450" style="border:0;" allowfullscreen="true" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>

  </div>
  <br>
  <a href="https://8048bf14c1.clvaw-cdnwnd.com/f80d7a5356be0d319861778d7e89b608/200002897-3efae3efb0/REQUISITOS%20matriculacion.pdf">Otras Sedes...</a>
  </section>
</template>

<style scoped>
.hero {
  background: linear-gradient(to right, #005bbb, #0078d4);
  color: white;
  padding: 0rem 2rem;
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
h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  text-align: center;
}
p {
  margin-bottom: 2rem;
  text-align: center;
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
.mapa {
  margin: 2rem 0;
  text-align: center;
}

.mapa-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
}

.mapa-contenedor {
  width: 600px;
  height: 500px;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
}



.mapa-contenedor iframe {
  width: 100%;
  height: 100%;
  border: 0;
}

</style>
