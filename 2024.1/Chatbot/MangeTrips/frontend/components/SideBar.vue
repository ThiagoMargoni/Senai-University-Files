<template>
    <div class="layout">
        <div id="sidebar" class="sidebar">
            <div class="sidebar-header">
                <div class="logo">
                    <div>M</div>
                    <h5>Mange Trips</h5>
                </div>
                <FloatingButton></FloatingButton>
            </div>
            <div class="sidebar-content">
                <nav class="menu">
                    <ul>
                        <li class="menu-header"><span> HISTORY </span></li>
                        <li class="menu-item sub-menu" v-for="history in messagesHistory" :key="history.id">
                            <NuxtLink :to="'/' + history.id">
                                <span class="menu-icon">
                                    <nuxt-icon name="MessageRound"></nuxt-icon>
                                </span>
                                <span class="menu-title" v-if="history.title">{{ history.title }}</span>
                                <span class="menu-title" v-else>Conversa - {{ history.date }}</span>
                            </NuxtLink>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </div>
</template>

<script setup>

    const { data: messagesHistory } = await useFetch('http://localhost:8000/conversation_history/1/', { key: 'getMessagesHistory' });

</script>

<style lang="scss">

.layout {
    overflow-x: hidden;
    width: 18vw;
    z-index: 1;
    
    a {
        text-decoration: none;
    }
    
    .sidebar {
        min-height: 100vh;
        background-color: var(--bg-color-sidebar);
        color: var(--text-color-sidebar);
        display: flex;
        flex-direction: column;
        z-index: 2;
        
        .sidebar-header {
            min-height: 100px;
            display: flex;
            align-items: center;
            padding: 0 20px;
            
            .logo {
                display: flex;
                align-items: center;
                
                div {
                    width: 35px;
                    min-width: 35px;
                    height: 35px;
                    min-height: 35px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    border-radius: 8px;
                    color: white;
                    font-size: 24px;
                    font-weight: 700;
                    background-color: var(--logo-color);
                    margin-right: 10px;
                }
                
                h5 {
                    margin-top: 2px;
                    overflow: hidden;
                    white-space: nowrap;
                    text-overflow: ellipsis;
                    font-size: 20px;
                    line-height: 30px;
                    transition: opacity 0.3s;
                    opacity: 1;
                }
            }
        }

        .sidebar-content {
            padding: 10px 0;

            .menu {
                .menu-header {
                    font-weight: 600;
                    padding: 10px 25px;
                    font-size: 0.8em;
                    letter-spacing: 2px;
                    transition: opacity 0.3s;
                    opacity: 0.5;
                }

                .menu-item {
                    a {
                        display: flex;
                        align-items: center;
                        height: 50px;
                        padding: 0 20px;
                        font-size: 17px;
                        margin-top: 1px;
                        color: var(--text-color-sidebar);
                    }

                    .menu-icon {
                        font-size: 23px;
                        width: 35px;
                        height: 35px;
                        line-height: 35px;
                        text-align: center;
                        margin-right: 6px;

                        i {
                            display: inline-block;
                        }
                    }
                }
            }
        }
    }
}
</style>