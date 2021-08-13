<template>

    <div>

        <div class="button-container">
            <button @click="exportFiles" v-if="contain_images">Download classifications</button>
        </div>
        <Image v-for="(img, index) of images" :key="index" :image="img"/>
        <div class="space"></div>

    </div>

</template>

<script>

    import Image from '../components/Image.vue'

    export default {

        data() {
            return {

            }
        },
        components: {
            Image
        },
        computed: {

            images(){
                return this.$store.state.predictions
            },
            contain_images(){
                return this.$store.state.predictions.length > 0
            }
        },
        methods: {
            exportFiles(){
                
                let predictions = this.$store.state.predictions

                for(let i = 0; i < predictions.length; i++){

                    var content = predictions[i].img;
                    var filename = "Predicted_to_" + predictions[i].prediction + "_" + predictions[i].file_name;
                    var blob = new Blob([content], {
                      type: "image/jpg"
                      });
                    saveAs(blob, filename);

                }               

            }

        },
        mounted(){

            if(!this.$store.state.predictions.length > 0){
                this.$router.push("/")
            }
        }
    }

</script>

<style scoped>

    button {
        width: 40%;
        height: 40px;
    }

    .space {
        height: 100px;
    }

    @media screen and (min-width: 601px) {

        button {
            font-size: 16px;
            margin-bottom: 50px;
            margin-top: 20px;
        }
    }

    @media screen and (max-width: 600px) {

        button {
            font-size: 13px;
            margin-bottom: 20px;
        }
    }

</style>