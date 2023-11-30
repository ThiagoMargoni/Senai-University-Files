<script setup>
    const route = useRoute();
    const id = route.params.id

    const { data: task } = await useFetch(`http://localhost:8000/tarefas/${id}`, {
        key: 'getCurrentTask'
    });

    const { data: responsibles } = await useFetch(`http://localhost:8000/tarefasUsuarios?tarefa=${id}`, {
        key: 'getCurrentResponsible'
    });

    const { data: statusTask } = await useFetch(`http://localhost:8000/tarefasStatus?tarefa=${id}`, {
        key: 'getStatusTask'
    });
</script>

<template>
    <div>
        <h1>{{ task.data.nome }}</h1>
        <h3>Actual Status: {{ task.data.idStatusFK.nome }}</h3>
        
        <div>
            <h4>Task Progress:</h4>
            <p v-for="status in statusTask.data" :key="status.id">
                Status: {{ status.idStatusFK.nome }} - Date and Time: {{ status.data }}
            </p>
        </div>

        <h3>Description: {{ task.data.descricao }}</h3>
        <p>Start Date: {{ task.data.dataInicio }} - End Date: {{ task.data.dataFim ? task.data.dataFim : 'Not Finished' }}</p>

        <h2>Requester: {{ task.data.idSolicitanteFK.nome }}</h2>
        <img :src="`${task.data.idSolicitanteFK.image}`" alt="">
        
        <section v-for="responsible in responsibles.data" :key="responsible.id">
            <h2>Responsible: {{ responsible.idUsuarioFK.nome }}</h2>
            <img :src="`${responsible.idUsuarioFK.image}`" alt="">
        </section>
    </div>
</template>