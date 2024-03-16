<template>
    <div>
        <div class="chat-history" v-for="(conversation, id) in conversationHistory" :key="id">
            <TextBox :name="conversation.name" :avatarImage="conversation.image" 
                :message="conversation.text" :type="conversation.type"/>
        </div>
        <hr>
        <div class="ask-question">
            <textarea placeholder="Type your question here" v-model="dialog.text"></textarea> <br> <br>        
            <Button @click="sendMessage" label="Send"></Button>
        </div>
    </div>
</template>

<script setup>
    let response = ref("")
    const dialog = reactive({
        text: '',
        type: '',
        name: '',
        image: '',
        historyId: null
    });

    const includeDialog = ((type)=>{
        if(type === 'Q'){
            dialog.image = 'user.png';
            dialog.name = 'André';            
            dialog.type = 'right';
        } else {
            dialog.image = 'bot.png';
            dialog.name = 'Bot';            
            dialog.type = 'left';
        }
        conversationHistory.value.push(
            JSON.parse(JSON.stringify(dialog))
        );                
    });
    
    const sendMessage = async () => {
        includeDialog('Q');
        
        const {data: answer} = await useFetch('http://localhost:8000/chatbot/',{
            method: 'POST',
            body:{
                question: dialog.text,
                userId: 1,
                conversationId: dialog.historyId
            }   
        })
        dialog.text = answer.value.message
        dialog.historyId = answer.value.history.id
        includeDialog('A');
        dialog.text = ''
    }

    const conversationHistory = ref([])

</script>

<style scoped lang="scss">
    // .chat-history {
    //     display: flex;
    //     justify-content: center ;
    // }

    .ask-question {
        display: flex;
        justify-content: center;
    }
</style>