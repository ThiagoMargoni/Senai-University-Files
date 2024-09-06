<script setup lang="ts">
    import { useCart } from '@/stores/cart';
    const cartStore = useCart();
</script>

<template>
    <div>
        <table>
            <thead>
                <th>Index</th>
                <th>Head</th>
                <th>Torso</th>
                <th>Base</th>
                <th>Left Arm</th>
                <th>Right Arm</th>
                <th>Cost</th>
                <th>Action</th>
            </thead>
            <tbody>
                <tr v-for="(robot, index) in cartStore.robots" :key="index">
                    <td>{{ index + 1 }}</td>
                    <td>{{ robot.head.title }}</td>
                    <td>{{ robot.torso.title }}</td>
                    <td>{{ robot.base.title }}</td>
                    <td>{{ robot.leftArm.title }}</td>
                    <td>{{ robot.rightArm.title }}</td>
                    <td>R${{ robot.cost }}</td>
                    <td><button @click="cartStore.removeCart(index)">Remove</button></td>
                </tr>
                <tr>
                    <td colspan="5"><strong>Total: R${{ cartStore.getTotalCost }}</strong></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>