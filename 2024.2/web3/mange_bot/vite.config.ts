import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    proxy: {
      '/proxy-api': {
        target: "https://mange-make-bot.azurewebsites.net",
        secure: false,
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/proxy-api/, '')
      }
    }
  },
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      '@Services': fileURLToPath(new URL('./src/services', import.meta.url)),
      '@Fonts': fileURLToPath(new URL('./src/assets/fonts', import.meta.url)),
      '@Styles': fileURLToPath(new URL('./src/assets/styles', import.meta.url)),
      '@Views': fileURLToPath(new URL('./src/views', import.meta.url)),
      '@Components': fileURLToPath(new URL('./src/components', import.meta.url))
    }
  }
})
