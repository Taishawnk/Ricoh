<script setup>
import TheWelcome from './components/TheWelcome.vue'
import VueLogo from './assets/Vue.png';
import { ref } from 'vue'; //re Vue.js instance properties that are used to register or indicate a reference to HTML elements or child elements in the template of your application. 
const props = defineProps({
  token: String, 
  user: String}) // creats props object and assigns them to the Vue instance passed in token and user from main.js file  ? means it is optional didnt have to pring in defineProps 
  //because it came with  script setup but this is not ture for ever built in vue 
 const token = props.token ? props.token : null  // going to be using this any time a request is made to the backend vue is specal in the fact that we don have to 
 //jump through alot of loops to get this functionality CSRF token needs to be on every single page for security so very useful to be able to do this in vue so ealily
 const username = props.user ? props.user : ''

let count = ref(0)

function increment(event){
  console.log(event)
  count.value++ 
}
</script>

<template>
  <header>
  
    {{ count }} - {{token}} - {{username}}
    <img 
  :src="VueLogo" 
  alt="Vue Logo" 
  class="logo" 
  width="125" 
  height="125" 
  @click="increment">
    <!--  @click creates clicke events in Vue -->
    <div class="wrapper"> 
    </div>
  </header>

  <main>
    <TheWelcome  />
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
