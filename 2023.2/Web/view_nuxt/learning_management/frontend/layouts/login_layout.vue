<script>
    export default {
        mounted() {
            if(localStorage.getItem('is_logged')) {
                this.$router.push('/tasks');
            }
        }
    }
</script>

<template>
    <div>
        <slot></slot>
    </div>
</template>