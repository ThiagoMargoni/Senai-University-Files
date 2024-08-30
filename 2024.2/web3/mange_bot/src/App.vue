<script setup lang="ts">
import { RouterView } from 'vue-router'
import FooterBot from '@Components/FooterBot.vue';
import Menu from '@Components/Menu.vue';
</script>

<template>

    <main id="card-app">
        
        <div id="content-app">
            <Menu></Menu>
            <RouterView />
        </div>

        <footer class="flex flex-row align-items-end justify-content-end">
            <div class="footer-bots flex flex-row justify-content-evenly">
                <FooterBot img="bot0.png" :text="$t('footer.technology')"></FooterBot>
                <FooterBot img="bot1.png" :text="$t('footer.platform')"></FooterBot>
                <FooterBot img="bot2.png" :text="$t('footer.support')"></FooterBot>
            </div>
            <!-- <img src="/icon2.png" id="circle"> -->
        </footer>
    </main>
</template>

<style scoped lang="scss">
    
    #card-app {
        width: 80%;
        height: 90%;
        background-color: var(--app-card-background);
        border-radius: 1.5rem;
        box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
    }

    #content-app {
        // height: calc(100% - 10rem);
        height: 80%;
        width: 100%;
    }

    footer {
        width: 100%;
        max-height: 20%;
        height: 20%;
        background-color: var(--app-footer-background);
        border-radius: 0 0 1.5rem 1.5rem;

        .footer-bots { 
            width: 80%;
            margin: auto;
        }

        // #circle{
        //     height: 100%;
        //     margin-right: 1.5rem;
        // }
    }

    // @media (max-height: 850px) {
    //     #content-app { 
    //         height: 80%;
    //     }
    // }

</style>