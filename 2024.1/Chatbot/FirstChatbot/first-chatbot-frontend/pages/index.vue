<template>
    <div>

        <div v-for="(conversation, id) in conversationHistory" :key="id">
            <TextBox :name="conversation.name" :avatarImage="conversation.image" :message="conversation.text"
                :type="conversation.type" />
        </div>

        <label for="text-message">Type your message here</label><br>
        <textarea id="text-message" v-model="dialog.text"></textarea><br><br>
        <Button @click="sendMessage" label="Send"></Button>
    </div>
</template>

<script setup>
    const dialog = reactive({
        name: '',
        image: '',
        text: '',
        type: ''
    })

    const includeDialog = (type) => {

        if (type === 'Q') {
            dialog.image = 'user.png';
            dialog.name = 'Thiago';
            dialog.type = 'right';
        } else {
            dialog.image = 'bot.png';
            dialog.name = 'Bot';
            dialog.type = 'left';
        }

        conversationHistory.value.push(
            JSON.parse(JSON.stringify(dialog))
        );
    }

    const sendMessage = async () => {

        includeDialog('Q');

        const { data: answer } = await useFetch('http://127.0.0.1:8000/chatbot/', {
            method: 'POST',
            body: {
                question: dialog.text
            }
        });

        dialog.text = answer.value.content;
        includeDialog('A');
    }

    const conversationHistory = ref([]);
</script>