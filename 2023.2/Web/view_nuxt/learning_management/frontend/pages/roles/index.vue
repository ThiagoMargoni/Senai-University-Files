<script setup>

    const { data: roles } = await useFetch('http://localhost:8000/cargos', {
        key: 'getAllRoles'
    });

</script>

<template>
    <div>
        <h1>Roles: </h1>
        <p v-for="role in roles.data" :key="role.id">
            {{ role.id }} - {{ role.nome }}
        </p>
    </div>
</template>