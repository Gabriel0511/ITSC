<template>
  <section class="contacto" id="contacto">
    <div class="contenido">
      <div class="texto">
        <h2>Contáctanos</h2>
        <p>Estamos aquí para responder todas tus dudas y ayudarte en tu proceso de inscripción.</p>
      </div>

      <form @submit.prevent="enviarFormulario" class="formulario">
        <label>
          Nombre completo
          <input v-model="nombre" type="text" placeholder="Tu nombre" required />
        </label>

        <label>
          Correo electrónico
          <input v-model="email" type="email" placeholder="tucorreo@ejemplo.com" required />
        </label>

        <label>
          Teléfono
          <input v-model="telefono" type="tel" placeholder="Tu número de teléfono" required />
        </label>

        <label>
          Curso de interés
          <select v-model="curso" required>
            <option disabled value="">Selecciona un curso</option>
            <option>Desarrollo Web</option>
            <option>Electricidad Industrial</option>
            <option>Administración</option>
            <option>Redes</option>
          </select>
        </label>

        <button type="submit">Enviar</button>
      </form>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const nombre = ref('')
const email = ref('')
const telefono = ref('')
const curso = ref('')

function enviarFormulario() {
  console.log('Datos enviados:', { nombre: nombre.value, email: email.value, telefono: telefono.value, curso: curso.value })
  alert('Gracias por contactarnos. Te responderemos pronto.')
}
</script>

<style scoped>
.contacto {
  background-color: #f8f9fa;
  padding: 4rem 2rem;
}
.contenido {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}
.texto {
  margin-bottom: 2rem;
}
.formulario {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  display: flex;
  flex-direction: column;
  gap: 1rem;
  text-align: left;
}
input, select {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 1rem;
}
button {
  background-color: #0056b3;
  color: white;
  border: none;
  padding: 0.75rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: bold;
}
button:hover {
  background-color: #003f88;
}
</style>
