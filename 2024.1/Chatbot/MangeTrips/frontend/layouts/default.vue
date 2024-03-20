<template>
    <div class="div-app">
        <SideBar></SideBar>
        <slot></slot>
    </div>
</template>

<style lang="scss">

.div-app {
    width: 100vw;
    height: 100vh;
    display: flex;
    background-color: var(--bg-color);
}

</style>