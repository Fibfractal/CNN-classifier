<template>

    <footer class = "footer">

        <p>&copy;2021 Pooler corperation</p>
        <p>pooler@pooler.com</p>

    </footer>

</template>

<script>
    export default {
    }
</script>

<style scoped>

    .footer {
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: rgb(206, 90, 90);
        box-shadow: 0px -5px 10px  0px;

        position: absolute;
        bottom: 0;
        width: 100%;
    }

    p{
        color: black;
    }

    /* If the screen size is 601px wide or more */
    @media screen and (min-width: 601px) {
        .footer {
            height: 70px;
        }

        p{
            font-size:18px;
            margin: 10px;
        }
    }

    /* If the screen size is 600px wide or less */
    @media screen and (max-width: 600px) {

        .footer {
            height: 50px;
        }

        p{
            font-size:14px;
            margin: 5px;
        }
    }

</style>