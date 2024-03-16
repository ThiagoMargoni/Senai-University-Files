<template>
    <div>
        <h1>BEM VINDO AO SITE</h1>
    </div>
</template>

<script setup lang="ts">
    definePageMeta({
        middleware: 'auth'
    })
</script>