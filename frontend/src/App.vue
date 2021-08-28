<template>
  <div>
    <main>
      <Navbar/>
      <router-view/>
      <Footer/>
    </main>
</div>

</template>

<script>

  import Navbar from './components/Navbar.vue'
  import Footer from './components/Footer.vue'

  export default {

    name: 'App',
    components: {
      Navbar,
      Footer
    },
  }

</script>

<style>

  main {
    width: 100vw;
  }

  ::-webkit-scrollbar {
      height: 0px;
  }

  ::-webkit-scrollbar-thumb {
    background-color: rgb(206, 90, 90,0.8);
    border: 1px solid #141414;
  }

  body::-webkit-scrollbar-track {
    background: rgb(185, 182, 182);
  }

</style>

