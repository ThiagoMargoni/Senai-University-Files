import { defineStore } from 'pinia';
import { Cart, ItemCart } from '@/models/cart';

export const useCart = defineStore('useCartStore', {
    state: (): Cart => ({
        robots: []
    }),
    actions: {
        addCart(item: ItemCart) {
            const deepCopy = JSON.parse(JSON.stringify(item)) as ItemCart;
            this.robots.push(deepCopy);

            // this.robots = [
            //     ...this.robots,
            //     item
            // ]
        },
        removeCart(index: number) {
            if(index < this.robots.length)
                this.robots.splice(index, 1);

        }
    },
    getters: {
        getTotalCost(): number {
            return this.robots.reduce((sum, robot) => sum + robot.cost, 0.0);
        }
    },
    persist: true
});