<template>
    <div>
        <label for="text-message">Type your message here</label><br>
        <textarea id="text-message" v-model="question"></textarea><br><br>
        <button @click="sendMessage">Send</button>
    </div>
</template>

<style scoped>
    button {
        background-color: black;
        color: white;
    }
</style>

<script setup>
    let question = ref('');

    const sendMessage = async () => {
        const { data: answer } = await useFetch('http://127.0.0.1:8000/chatbot/', {
            method: 'POST',
            body: {
                question: question
            }
        })
    }
</script>