<template>

    <nav>
        <div class="img_wrap">
            <img src="..\assets\logo.svg" width=50 height=50 class="logo">
            <p>Pooler</p>
        </div>

        <div class="links" v-if="contain_images">

            <div class="container">
                <router-link active-class="active" to="/">Import images</router-link>
                <router-link active-class="active" to="/predictions">Classification</router-link>
                <router-link active-class="active" to="/statistics">Diagram</router-link>
            </div>
        </div>
    </nav>

</template>

<script>

    export default {

        computed: {

            contain_images(){
                return this.$store.state.predictions.length > 0
            }
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

    .active {
        text-decoration-line: underline;
        text-underline-offset: 0.3em
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

    p {
        font-weight: bold;
        color: white;
    }

    .img_wrap {
        float: left;
    }

    /* If the screen size is 601px wide or more*/
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

    /* If the screen size is 600px wide or less*/
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