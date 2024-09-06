import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPlugin from 'pinia-plugin-persistedstate';
import '@Styles/global.scss';
import { i18nApplication } from './assets/i18n/i18n';

import App from './App.vue'
import router from './router'

const app = createApp(App)

const pinia = createPinia();
pinia.use(piniaPlugin);

app.use(pinia);
app.use(router);
app.use(i18nApplication);

app.mount('#app')