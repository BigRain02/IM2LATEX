<template>
    <div id="app">
        <img alt="Vue logo" src="./assets/logo.png">
        <HelloWorld msg="Welcome to Your Vue.js App"/>
        <ImageUploader @upload-success="handleUploadSuccess"/>
        <div v-if="latexStr">
            <LatexRender>
                <p>
                    \[
                    {{ latexStr }}
                    \]
                </p>
            </LatexRender>
            <button @click="copyToClipboard">Copy LaTeX Code</button>
        </div>
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
    },
    data() {
        return {
            latexStr: ''
        };
    },
    methods: {
        handleUploadSuccess(latexStr) {
            this.latexStr = latexStr;
        },
        copyToClipboard() {
            const el = document.createElement('textarea');
            el.value = this.latexStr;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
            alert('LaTeX code copied to clipboard!');
        }
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
