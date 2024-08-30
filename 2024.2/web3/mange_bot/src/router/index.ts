import { createRouter, createWebHistory } from 'vue-router'
import BuildView from '@Views/BuildView.vue';
import CartView from '@Views/CartView.vue';
import HomeView from '@Views/HomeView.vue';
import NotFoundView from '@/views/NotFoundView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/build',
      name: 'Build',
      component: BuildView
    },
    {
      path: '/cart',
      name: 'Cart',
      component: CartView
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: NotFoundView
    }
  ]
})

export default router
