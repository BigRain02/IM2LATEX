<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <ImageUploader />
    <LatexRender>
      <p>
        \[
        \int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
        \]
      </p>
    </LatexRender>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import ImageUploader from './components/ImageUploader.vue';
import LatexRender from './components/LatexRender.vue';

export default {
  name: 'App',
  components: {
    HelloWorld,
    ImageUploader,
    LatexRender
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
