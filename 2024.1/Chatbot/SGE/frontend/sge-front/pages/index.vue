<template>
    <main class="login-main flex-center">
        <section class="logo-panel flex-center">
            <img src="/sge.jpeg" alt="sge logo">
            <h1>Sistema de Gestão de Ensino</h1>
            <p> &reg; Senai Roberto Mange </p>
            <div class="stars1"></div>
            <div class="stars2"></div>
            <div class="stars3"></div>
        </section>

        <section class="login-panel">
            <div class="login-content flex-center">
                <h1>LOGIN</h1>
                <form action="" class="login-form" v-on:submit.prevent="submitLogin">
                    <div class="input-container">
                        <CustomInput label="LOGIN" inputId="user-login" 
                            v-model="credentials.username"></CustomInput>
                    </div>

                    <div class="input-container">
                        <CustomInput label="SENHA" type="password" 
                            inputId="pass-login" v-model="credentials.password"></CustomInput>
                    </div>
                    <button type="submit" class="custom-button">ENTRAR</button>
                </form>
            </div>
        </section>
    </main>
</template>

<script lang="ts" setup>
    const { signIn } = useAuth();

    definePageMeta({
        middleware: 'auth',
        auth: {
            navigateAuthenticatedTo: '/home'
        }
    });

    const credentials = reactive({
        username: '',
        password: ''
    })

    const submitLogin = async () => {
        signIn(credentials, { redirect: false })
        .then(() => {
            navigateTo('/home')
        }).catch((error) => console.log(error));
    }
</script>

<style lang="scss">

    .flex-center {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
    }

    .login-main {
        width: 100vw;
        height: 100vh;
        background-color: var(--dark-background);

        .logo-panel {
            display: none;
            width: 50vw;
            height: 100vh;
            flex-direction: column;
            color: var(--light-background);

            img {
                margin: 0 0 25px 0;
                align-items: center;
                width: 65%;
                height: 45%;
            }
        }

        .login-panel {
            width: 100vw;
            height: 100vh;
            background-color: var(--light-background);

            .login-content {
                flex-direction: column;
                width: 100%;
                height: 80%;
            }

            h1 {
                width: 120px;
                padding-top: 10px;
                padding-bottom: 50px;
                font-size: 36px;
            }

            .login-form {
                width: 60%;
                
                .input-container {
                    margin-top: 30px;
                }

                .custom-button {
                    margin-top: 50px;
                }
            }
        }
    }

    @media screen and (min-width: 550px) {
        .login-main {
            .login-panel {
                width: 50vw;
            }
            
            .logo-panel {
                display: flex;
            }
        }
    }
</style>