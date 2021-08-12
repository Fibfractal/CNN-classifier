<template>

    <nav>
        <p>LOGO</p>
        <router-link to="/">Import images</router-link>
        <router-link to="/predictions">Classification</router-link>
        <router-link to="/statistics">Diagram</router-link>
    </nav>

</template>

<script>

    export default {

        data() {
            return {

            }
        },
        methods: {

        }

    }

</script>

<style scoped>

    nav {
        display:flex;
        justify-content: space-around;
        background-color:rgb(206, 90, 90);
        margin-bottom: 40px;
        height: 60px;
        color: black;
        box-shadow: 0px 5px 10px  0px;
    }

    a {
        text-decoration: none;
        font-size: 20px;
        color: black;
        margin: 10px;
    }

    a:hover {
        color: white;
        transition: 0.5s;
    }

</style>