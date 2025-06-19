<template>
  <div>
    <AppNavbar />
    <Hero />
    <Features />
    <Carreras />
    <SobreNosotros />
    <CTASection />
    <ContactoForm />
  </div>
</template>

<script setup>
import AppNavbar from './components/AppNavbar.vue'
import Hero from './components/HeroSection.vue'
import Features from './components/FeaturesSection.vue'
import Carreras from './components/CarrerasSection.vue'
import SobreNosotros from './components/SobreNosotros.vue'
import CTASection from './components/CTASection.vue'
import ContactoForm from './components/contactoForm.vue'
</script>
