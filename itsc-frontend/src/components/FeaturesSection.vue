<template>
  <section class="features">
    <h2>¿Por qué elegirnos?</h2>
    <p class="desc">Comprometidos con la excelencia educativa y la formación integral de nuestros estudiantes.</p>
    <div class="cards">
      <div class="card" v-for="feature in features" :key="feature.title">
        <div class="icon">{{ feature.icon }}</div>
        <h3>{{ feature.title }}</h3>
        <p>{{ feature.text }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
const features = [
  {
    icon: '📘',
    title: 'Profesores Calificados',
    text: 'Equipo docente con amplia experiencia y capacitación en sus áreas.'
  },
  {
    icon: '📜',
    title: 'Certificación Oficial',
    text: 'Cursos con certificación oficial reconocida por el Ministerio de Educación.'
  },
  {
    icon: '🏢',
    title: 'Instalaciones Modernas',
    text: 'Aulas equipadas con tecnología para formación práctica y de calidad.'
  }
]
</script>

<style scoped>
.features {
  text-align: center;
  padding: 4rem 2rem;
  background-color: #f9fafb;
}
.desc {
  max-width: 600px;
  margin: 0 auto 2rem;
}
.cards {
  display: flex;
  gap: 2rem;
  justify-content: center;
  flex-wrap: wrap;
}
.card {
  background: white;
  padding: 1.5rem;
  border-radius: 10px;
  width: 300px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.icon {
  font-size: 2rem;
  margin-bottom: 1rem;
}
</style>
