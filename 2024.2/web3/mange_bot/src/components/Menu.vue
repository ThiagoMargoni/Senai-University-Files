<script setup lang="ts">
    import { changeLanguage, i18nApplication, type AvailableLanguages } from '@/assets/i18n/i18n';
    import { computed, ref, type Ref } from 'vue';

    const currentLanguage: Ref<AvailableLanguages> = 
        ref(i18nApplication.global.locale.value);

    const onChangeLanguage = () => {
        if(currentLanguage.value === 'pt_br') {
            changeLanguage('en_us');
        } else {
            changeLanguage('pt_br');
        }

        currentLanguage.value = i18nApplication.global.locale.value;
    };

    const flag = computed(() => currentLanguage.value == 'en_us' ? 'en.webp' : 'br.webp');
</script>

<template>
    <header class="flex flex-row align-items-center ">
        <nav class="ml-5">
            <img src="/build-a-bot-logo.png" alt="robot logo">
            <RouterLink class="m-4" to="/">{{ $t('header.home') }}</RouterLink>
            <RouterLink class="m-4" to="/build">{{ $t('header.build') }}</RouterLink>
            <RouterLink class="m-4" to="/cart">{{ $t('header.cart') }}</RouterLink>
        </nav>
        <img id="flag" :src="flag" alt="flag" @click="onChangeLanguage">
    </header>
</template>

<style scoped lang="scss">

    header {
        height: 5rem;
        width: 100%;
        margin-top: 0.5%;
        justify-content: space-between;

        nav {
            display: flex;
            justify-content: center;
            
            img {
                margin-left: 4rem;
                margin-right: 20px;
                height: 4rem;
            }

            a {
                text-decoration: none;
                font-size: 1.5rem;
                color: var(--app-dark-text-color);
            }

            .router-link-exact-active {
                font-weight: bold;
            }
        }

        #flag {
            height: 2.5rem;
            width: 3.5rem;
            margin-right: 7%;
            cursor: pointer;
        }
    }

</style>