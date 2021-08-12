<template>

    <nav>
        <p>LOGO</p>

        <div class="links">

            <div class="container">
                <router-link to="/">Import images</router-link>
                <router-link to="/predictions">Classification</router-link>
                <router-link to="/statistics">Diagram</router-link>
            </div>
        </div>
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
        align-items: center;
        background-color:rgb(206, 90, 90);
        margin-bottom: 40px;
        height: 70px;
        color: black;
        box-shadow: 0px 5px 10px  0px;
    }

    .links {
        margin: auto;
    }

    .container {
        display: flex;
        justify-content: center;
    }

    a {
        text-decoration: none;
        color: black;
    }

    a:hover {
        color: white;
        transition: 0.5s;
    }

    p {
        float: left;
    }

    /* If the screen size is 601px wide or more, set the font-size of <div> to 22px */
    @media screen and (min-width: 601px) {
        a {
            font-size: 22px;
            margin-left: 30px;
            margin-right: 30px;
        }
    }

    /* If the screen size is 600px wide or less, set the font-size of <div> to 10px */
    @media screen and (max-width: 600px) {
        a {
            font-size: 15px;
            margin-left: 10px;
            margin-right: 10px;
        }
    }

</style>