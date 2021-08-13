<template>

    <nav>
        <div class="img_wrap">
            <img src="..\assets\logo.svg" width=50 height=50 class="logo">
            <p>Pooler</p>
        </div>

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
        font-weight: bold;
        color: white;
    }

    .img_wrap {
        float: left;
    }

    /* If the screen size is 601px wide or more, set the font-size of <div> to 22px */
    @media screen and (min-width: 601px) {
        a {
            font-size: 22px;
            margin-left: 30px;
            margin-right: 30px;
        }

        p {
            margin-left: 15px;
            font-size: 25px;
        }

        .logo {
            margin-left: 20px;
        }

        .img_wrap {
            display:flex;
            justify-content: center;
            align-items: center;
        }
    }

    /* If the screen size is 600px wide or less, set the font-size of <div> to 10px */
    @media screen and (max-width: 600px) {
        a {
            font-size: 15px;
            margin-left: 10px;
            margin-right: 10px;
        }

        p {
            margin-left: 10px;
            margin-bottom: 10px;
            font-size: 17px;
        }

        .logo {
            margin-left: 0px;
            width:30px;
            height:30px;
        }

        .img_wrap {
            display: inline;
        }
    }

</style>