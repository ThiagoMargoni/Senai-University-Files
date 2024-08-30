import { createApp } from 'vue'
import { createPinia } from 'pinia'
import '@Styles/global.scss';
import { i18nApplication } from './assets/i18n/i18n';

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(i18nApplication);

app.mount('#app')