<template>
    <div>
        <div class="floating-button">
            <NuxtLink to="/">
                <nuxt-icon name="Plus" style="color: white;"></nuxt-icon>
            </NuxtLink>
        </div>
    </div>
</template>

<style lang="scss">

    .floating-button {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        border-radius: 100%;
        background-color: transparent;
        font-size: 25px;
        font-weight: bold;
        margin-left: 30px;
        border: 1px solid white;
    }

</style>