<script setup>
    definePageMeta({
        layout: "login-layout"
    });

    const { data: users } = await useFetch('http://localhost:8000/usuarios', {
        key: 'getAllUsers'
    });

    const selectOption = () => {
        document.querySelector('#button_submit').disabled = document.querySelector('#login_forms').value === '';
    }

    const clickedLogin = () => {
        localStorage.setItem('is_logged', true)
    }
</script>

<template>
    <div>
        <section style="display: grid; justify-content: center; justify-items: center;">
            <h1>Welcome to Hogwarts University Learning Management</h1>
            <img src="../assets/logo.png" alt="" width="100" height="200">
        </section>

        <form style="display: flex; justify-content: center; margin-top: 50px; height: 100px;">
            <div style="display: flex; justify-content: space-evenly; flex-direction: column; ">
                <select name="login_forms" id="login_forms" @change="selectOption()">
                    <option value="" selected>Choose your email to login</option>
                    <option v-for="user in users.data" :value="user.email" :key="user.id">{{ user.email }}</option>
                </select>

                <NuxtLink to="/tasks">
                    <button @click="clickedLogin()" type="submit" id="button_submit" style="width: 100%;" disabled>Login</button>
                </NuxtLink>
            </div>
        </form>
    </div>
</template>