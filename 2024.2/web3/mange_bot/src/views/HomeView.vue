<script setup lang="ts">
    import { useRouter } from 'vue-router';

    const router = useRouter();
</script>

<template>
    <div id="div" class="flex flex-row align-items-center justify-content-evenly">
        <section class="flex flex-column align-items-center">
            <h1>{{ $t('home.title') }}</h1>
            <button id="order" @click="router.push('/build')" class="mt-4 app-dark-button">{{ $t('home.order') }}</button>
        </section>

        <section>
            <img src="/big-bot.png" alt="robot">
        </section>
    </div>
</template>

<style scoped lang="scss">

    #div {
        height: 80%;
    }
    
    h1 {
        font-size: 5rem;
        width: 25rem;
        text-align: center;
    }

    #order {
        height: 3.2rem;
        width: 20rem;    
        border-radius: 2.5rem;    
    }

</style>