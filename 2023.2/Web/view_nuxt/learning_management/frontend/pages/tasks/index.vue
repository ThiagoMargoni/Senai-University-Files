<script setup>
    const { data: tasks } = await useFetch('http://localhost:8000/tarefas?all', { 
        key: 'getAllTasks'
    });
</script>

<template>
    <div>
        <h1>All Tasks: </h1>

            <hr>
            <section v-for="task in tasks.data" :key="task.id">
                <NuxtLink :to="`/tasks/${task.id}`">
                    <p>{{ task.nome }}</p>
                </NuxtLink>
                <p>Local: {{ task.idAmbienteFK.nome }}</p>
                <p>Status: {{ task.idStatusFK.nome }}</p>
                <p>Deadline: {{ task.prazo }}</p>
            <hr>
            </section>
    </div>
</template>