<template>

    <div>

        <button @click="exportFiles" v-if="contain_images">Download classifications</button>
        <div id = "container">
            <div v-if="!contain_images" id = "message-container">
                <p >Import the images first, to classify</p>
            </div>
        </div>

        <Image v-for="(img, index) of images" :key="index" :image="img"/>

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

        }
        

    }

</script>

<style scoped>

    button {
        width: 40%;
        height: 40px;
        font-size: 16px;
        margin-bottom: 30px;
    }

    #container {
        display:flex;
        justify-content: center;

    }

    #message-container {
        display:flex;
        justify-content: center;
        margin-top: 30px;
        align-items: center;
        background-color: rgb(202, 72, 72);
        height: 50px;
        width: 80%;
    }

    p {
        color: white;
        font-size: 17px;
        font-weight: bold;
    }
    


</style>