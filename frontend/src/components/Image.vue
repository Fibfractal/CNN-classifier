<template>

    <div class = "image">
      <img :src="image.img_url">
      <p>Prediction: {{image.prediction}}</p>
      <p>Probability: {{image.probability}}</p> 
    </div>

</template>

<script>

  export default {
    
    props: ["image"],
    methods: {
 
    }

  }

</script>

<style scoped>

    p {
      display:flex;
      justify-self: flex-start;
      font-size: 20px;
      color: black;
      margin: 8px;
    }

    .image {
      display: inline-block;
      width: 200px;
      border: 1px solid black;
      background-color: rgb(206, 90, 90,0.8);
      margin: 8px;
      box-shadow: 0px 5px 10px  0px;


    }

    img {
      width: 60px;
      height: 60px;
      margin: 8px;
    }


    


</style>