<template>
    <div>
        <h1>BEM VINDO AO SITE</h1>

        <button class="custom-button" @click="logout">SAIR</button>
    </div>
</template>

<script setup lang="ts">
    const { signOut } = useAuth();

    definePageMeta({
        middleware: 'auth'
    })

    const logout = async () => {
        await signOut({ redirect: false })
        .catch((error) => console.log(error));
        navigateTo('/');
    }
</script>