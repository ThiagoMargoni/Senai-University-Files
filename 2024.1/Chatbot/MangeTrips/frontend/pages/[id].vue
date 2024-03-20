<template>
    <div class="chat-component">
        <div class="chat-history">
            <div class="chat-message" v-for="(conversation, id) in conversationHistory" :key="id">
                <TextBox :name="conversation.name" :avatarImage="conversation.image" 
                    :message="conversation.text"/>
            </div>
        </div>
        <div class="ask-question">
            <div class="question-area-style">
                <textarea @keydown="sendMessageEnter" placeholder="Type your question here" v-model="dialog.text" contenteditable></textarea>   
                <Button @click="sendMessage">
                    <nuxt-icon name="ArrowRight" class="send-icon"></nuxt-icon>
                </Button>
            </div>
        </div>
    </div>
</template>

<script setup>
    const router = useRoute();
    const id = router.params.id;

    const dialog = reactive({
        text: '',
        type: '',
        name: '',
        image: '',
        historyId: id
    });

    const includeDialog = ((type)=>{
        if(type === 'Q'){
            dialog.image = 'user.png';
            dialog.name = 'Thiago';
        } else {
            dialog.image = 'bot.png';
            dialog.name = 'Bot';
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
                title: null,
                question: dialog.text,
                userId: 1,
                conversationId: dialog.historyId
            }   
        })

        let dialogText = answer.value.message;
        dialog.text = dialogText;
        dialog.historyId = answer.value.history.id
        includeDialog('A');
        dialog.text = ''
    }

    const sendMessageEnter = async (e) => {
        if(e.code === "Enter") await sendMessage();
    }
    
    const { data } = await useFetch(`http://localhost:8000/conversation_messages/${id}/`, { key: 'getMessageHistory' })

    const dataValue = data.value;

    if(!dataValue) {
        throw createError({ statusCode: 404, statusMessage: 'Page Not Found' })
    }
    
    const conversationHistory = ref([])

    for(let index in dataValue) {
        if(dataValue[index].type === 'Q'){
            dialog.image = 'user.png';
            dialog.name = 'Thiago';
        } else {
            dialog.image = 'bot.png';
            dialog.name = 'Bot';
        }

        dialog.text = dataValue[index].message;

        conversationHistory.value.push(
            JSON.parse(JSON.stringify(dialog))
        );   
    }

    dialog.text = '';
</script>

<style scoped lang="scss">

    .chat-component {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100vw;
        overflow: hidden;

        .chat-history {
            width: 54vw;
            max-height: 86vh;
            justify-content: center;
            align-items: center;
            flex-direction: row;
            margin-top: -80px;
            overflow-y: auto;
        }

        .ask-question {
            display: flex;
            justify-content: center;
            align-items: center;
            position: fixed;
            bottom:0;
            left: 14vw;
            width: 86vw;
            height: 100px;

            .question-area-style {
                display: flex;
                justify-content: center;
                align-items: center;
                border: black 1px solid;
                border-radius: 15px;
                width: 54vw;
                height: 52px;
                
                textarea {
                    margin-top: 3px;
                    resize: none;
                    border: none;
                    overflow: auto;
                    outline: none;
                    width: 50vw;
                    height: 26px;
                    background-color: transparent;
                    font-size: 17px;
                    text-align: left;
                }
    
                button {
                    width: 40px;
                    height: 40px;
                    border-radius: 10px;
                    margin-left: 25px;
                    background-color: var(--logo-color);
                    border: none;
                    justify-content: center;
                    align-items: center;
    
                    .send-icon {
                        color: var(--bg-color);
                        font-size: 40px;
                    }
                }
            }

        }

    }
</style>