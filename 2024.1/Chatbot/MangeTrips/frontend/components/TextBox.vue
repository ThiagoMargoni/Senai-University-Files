<template>
    <div class="text-box">
        <Fieldset>
            <template #legend>
                <div class="avatar-class">
                    <Avatar :image="props.avatarImage" shape="circle"/>
                    <span class="font-bold"> {{ props.name }}</span>
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
    avatarImage: { type: String },
    name: { type: String },
    message: { type: String }
})

/* modo de comunicar props e css mais indicado quando não há tantas variações
const cardStyle = computed(()=> props.type === 'right' ? 
    {
        backColor: 'red',
        fontSize: '1.5rem',
        textColor: 'white'
    } 
: 
    {
        backColor: 'black',
        fontSize: '3.5rem',
        textColor: 'yellow'
    }    
)*/

</script>

<style scoped lang="scss">

.text-box {
    width: 1000px;
    margin-top: 20px;
    
    .p-fieldset {
        background-color: transparent !important;
        font-size: 1rem;
        color: black;

        .p-fieldset-legend, legend {
            background-color: transparent !important;
            background: transparent !important;
        }

        .avatar-class {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 10px;

            span {
                margin-left: 6px;
            }
        }
    }
}

/* 
.p-fieldset{
    background-color: v-bind(cardStyle.backColor);
    font-size: v-bind(cardStyle.fontSize);
    color: v-bind(cardStyle.textColor);
}*/

/* .right-style {
    .p-fieldset {
        background-color: rgb(180, 180, 219);
    }
}

.left-style {
    .p-fieldset {
        background-color: rgb(208, 167, 175);
    }
}*/
</style>