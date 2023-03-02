<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <TestDrive></TestDrive>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import TestDrive from "@/components/TestDrive";

export default {
  name: 'App',
  components: {
    TestDrive,
    HelloWorld
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
