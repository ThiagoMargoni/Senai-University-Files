<script setup>
    const { data: images } = await useFetch('http://localhost:8000/image');
</script>

<template>
    <div>
        <section v-for="element in images.results" :key="element.id">
            <h3>{{ element.tripFk }} - {{ element.title }}</h3>
            <NuxtLink :to="`/trips/${element.tripFk}`">
                <img :src="element.link" alt="Imagem Viagem">
            </NuxtLink>
        </section>
    </div>
</template>