<template>

    <div id = "container">

        <div class="statistics" v-if="contain_images">
            <h1>Number of each label</h1>

            <div id="canvas-container">
                <div id = "myCanvas">
                    <canvas id="myChart" v-if="contain_images"></canvas>

                </div>
            </div>
        </div>

    </div>
</template>

<script>
    // npm i chart.js@2.9.4 funkar   !!!!version 3.5.0 funkar inte!!!
    import Chart from 'chart.js'

    export default {

        data() {
            return {

                canvas: '',
                chart: ''

            }
        },
        components: {
        },
        computed: {

            contain_images(){
                return this.$store.state.predictions.length > 0
            }

        },
        methods: {
            createChart(counter){

                this.chart = new Chart(this.canvas, {
                    type:'bar',
                    data: {

                        labels: ['0','1', '2', '3', '4', '5', '6', '7', '8', '9'],
                        datasets: [
                            {
                                label: 'Nbr of each label',
                                data: counter,
                                backgroundColor: ['rgb(206, 90, 90,0.6)', 'rgb(206, 90, 90,0.6)', 'rgb(206, 90, 90,0.6)', 'rgb(206, 90, 90,0.6)',
                                                    'rgb(206, 90, 90,0.6)', 'rgb(206, 90, 90,0.6)', 'rgb(206, 90, 90,0.6)', 'rgb(206, 90, 90,0.6)', 
                                                    'rgb(206, 90, 90,0.6)','rgb(206, 90, 90,0.6)'],
                                // borderColor: ['rgb(206, 90, 90,0.8)'],
                                borderWidth: 1
                            }  
                        ],
                    },
                    options: {
                        scales: {
                            yAxes: [{
                                ticks: {
                                    beginAtZero: true,
                                    callback: function(value, index, values) {
                                        return value;
                                    }
                                }
                            }]
                        }
                    }
                })
                
            }
        },
        mounted(){

            if(this.$store.state.predictions.length > 0){

                let counter = this.$store.state.countedLabels
                let canvas = document.getElementById("myChart")
                this.canvas = canvas.getContext("2d")
                this.createChart(counter)
                console.log("Loaded!")
            }
            else {
                this.$router.push("/")
            }
        }
    }

</script>

<style scoped>

    #container {

        display:inline-block;
        width: 80%;
    }

    h1 {
        margin-bottom: 50px;
    }

    .statistics {
        margin-top: 20px;
    }

    #canvas-container {
        display: inline-block;
        width: 80%;
    }

    @media screen and (max-width: 600px) {

        h1 {
            font-size: 20px;
        }
    }
</style>