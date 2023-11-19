<script setup>

import TheWelcome from './components/TheWelcome.vue'
const props = defineProps({
  token: String, 
  user: String}) // creats props object and assigns them to the Vue instance passed in token and user from main.js file  ? means it is optional didnt have to pring in defineProps 
  //because it came with  script setup but this is not ture for ever built in vue 
  console.log(props.token)
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="/staticFiles/static/vue-dev/assets/logo-277e0e97.svg" width="125" height="125" />
    {{props.token}}
    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
