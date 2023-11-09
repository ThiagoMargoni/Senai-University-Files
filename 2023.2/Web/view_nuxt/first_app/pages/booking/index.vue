<script setup>
    const { data: bookings } = await useFetch('http://localhost:8000/booking');
</script>

<template>
    <div>
        <h1>All Bookings</h1>

        <div v-for="booking in bookings.results" :key="booking.id">
            <h1>Booking {{ booking.customUserFK }}</h1>
            <p>Start Date: {{ booking.startDate }}</p>
            <p>End Date: {{ booking.endDate }}</p>
            <p>Purchase Value: US${{ booking.purchaseValue }}</p>
        </div>
    </div>
</template>