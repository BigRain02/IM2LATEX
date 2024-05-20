<template>
  <div ref="mathContent">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'MathRenderer',
  mounted() {
    this.renderMath();
  },
  updated() {
    this.renderMath();
  },
  methods: {
    renderMath() {
      if (window.MathJax) {
        window.MathJax.typesetPromise([this.$refs.mathContent])
            .then(() => {
              console.log('MathJax: Typeset completed.');
            })
            .catch((err) => console.log('MathJax: Typeset failed: ', err));
      }
    }
  }
}
</script>
