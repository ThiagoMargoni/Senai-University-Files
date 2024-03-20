// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: false },
  typescript: {
    typeCheck: true
  },
  modules: [
    'nuxt-primevue',
    'nuxt-icons'
  ],
  primevue: {
    components: {
      include: ['Button', 'Fieldset', 'Avatar']
    }    
  },
  css: [
    'primevue/resources/themes/aura-light-green/theme.css',
    '~/assets/style/global.scss', 
    '~/assets/style/variables.scss'
  ]
})