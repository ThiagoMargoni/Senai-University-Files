<template>
    <div class="custom-input-field">
        <label :for="props.inputId">{{ props.label }}</label>
        <input v-model="model" :id="props.inputId" :type="props.type">
    </div>
</template>

<script setup lang="ts">
    const model = defineModel();

    const props = defineProps({
        label: {type: String, required: true},
        type: {type: String, default: 'text'},
        inputId: {type: String, required: true, default: 'custom-input'}
    });
</script>

<style scoped lang="scss">
    .custom-input-field {
        overflow-y: hidden;

        label {
            width: 100%;
            color: black;
        }

        input {
            width: 100%;
            padding: 10px;
            border: 0;
            border-bottom: 2px solid black;
            font-size: 20px;
            &:focus {
                outline: 0;
                border-color: crimson;
            }
        }
    }
</style>