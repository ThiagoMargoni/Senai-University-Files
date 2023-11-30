<script setup>

    let visible = false
    const changeFormsView = () => {
        visible = !false;
        refreshNuxtData();
    }

    const { data: ambients } = await useFetch('http://localhost:8000/ambientes', {
        key: 'getAllAmbients'
    });


    let name;
    const createAmbient = async () => {
        await useFetch('http://localhost:8000/ambientes/', {
            method: 'POST',
            body: [
                {
                    nome: name
                }
            ],
            key: 'postNewAmbient'
        });

        location.reload();
    }

</script>

<template>
    <div>
        <h1>Ambients: </h1>
        <p v-for="ambient in ambients.data" :key="ambient.id">
            {{ ambient.id }} - {{ ambient.nome }}
        </p>
        <hr>

        <button @click="changeFormsView()">Insert new ambient</button>
        <section v-if="visible">
            <label for="input_ambient">Insert the name: </label>
            <input type="text" v-model="name" id="input_ambient" required>
            <button @click="createAmbient()">Create</button>
        </section>
    </div>
</template>