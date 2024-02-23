<template>
    <div :class="props.type === 'right' ? 'right' : 'left'" class="common-class">
        <Fieldset>
            <template #legend>
                <div class="flex align-items-center pl-2">
                    <Avatar :image="props.avatarImage" shape="circle" />
                    <span class="font-bold">{{ props.name }}</span>
                </div>
            </template>
            <p class="m-0">
                {{ props.message }}
            </p>
        </Fieldset>
    </div>
</template>

<script setup>
    const props = defineProps({
        avatarImage: {type: String},
        name: {type: String},
        message: {type: String},
        type: {type: String}
    })

    // Modo indicado para poucas variações
    // const cardStyle = computed(() => props.type === 'right' ? 
    // {
    //     backgroundColor: 'red',
    //     fontSize: '1.5rem',
    //     textColor: 'white'
    // } : 
    
    // {
    //     backgroundColor: 'black',
    //     fontSize: '3.5rem',
    //     textColor: 'yellow'
    // });
</script>

<style scoped lang="scss">
    
    .common-class {
        .p-fieldset {
            font-size: 1rem;
            color: black;
        }
    }

    .right {
        .p-fieldset {
            background-color: #8686ce;
        }
    }

    .left {
        .p-fieldset{
            background-color: pink;
        }
    }

    /* Modo indicado para poucas variações
    .p-fieldset {
        background-color: v-bind(cardStyle.backgroundColor);
        font-size: v-bind(cardStyle.fontSize);
        text-color: v-bind(cardStyle.textColor);
    } */
</style>