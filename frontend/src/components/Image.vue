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
      color: black;
      margin: 8px;
    }

    .image {
      display: inline-block;
      border: 1px solid black;
      background-color: rgb(206, 90, 90,0.8);
      margin: 8px;
      box-shadow: 0px 5px 10px  0px;
    }

    img {
      margin: 8px;
    }

    /* If the screen size is 601px wide or more*/
    @media screen and (min-width: 601px) {
      p {
        font-size: 20px;
      }

      .image {  
        width: 200px;
      }

      img {
        width: 60px;
        height: 60px;
        margin-top:15px;
      }

    }

    /* If the screen size is 600px wide or less*/
    @media screen and (max-width: 600px) {
      p {
        font-size: 13px;
      }

      .image {  
        width: 130px;
      }

      img {
        width: 50px;
        height: 50px;
        margin-bottom: 0px;
      }
    }
    


</style>