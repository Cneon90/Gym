<template>

<!--    <img alt="Vue logo" src="./assets/logo.png">-->
<!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
<!--    <TestDrive></TestDrive>-->
 <section>


   {{ message }}

  <button @click="clickMe"> test  </button>
 </section>



</template>

<script>




export default {
  name: 'App',
  components: {

  },
    methods: {
            clickMe() {
               alert(2);
            }
        },
 data() {
    return { message: 4 }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
