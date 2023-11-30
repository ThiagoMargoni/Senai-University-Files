<script>
    export default {
        mounted() {
            if(!localStorage.getItem('is_logged')) {
                this.$router.push('/');
            }
        }
    }
</script>

<template>
    <div>
        <Menu></Menu>
        <slot></slot>
    </div>
</template>