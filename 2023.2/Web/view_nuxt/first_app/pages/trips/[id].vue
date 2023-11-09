<script setup>
    const route = useRoute();
    
    const { data: trip } = await useFetch(`http://localhost:8000/trip/${route.params.id}`);
    const { data: availabilitys } = await useFetch(`http://localhost:8000/availability?tripFk=${route.params.id}`);

</script>

<template>
    <div>
        <!-- <p :class="variavelAtributo"> {{variavelAtributo2}} </p> -->

        <h1>Welcome to trip {{ trip.title }}</h1>
        <p> {{ trip.description }} </p>
        <p> Daily: US${{ trip.daily }}</p>
        <p> Address: {{ trip.address }}</p>

        <h3>Available Dates</h3>
        <div v-for="availability in availabilitys.results" :key="availability.id">
            <p>{{ availability.date }}</p>
        </div>
    </div>
</template>