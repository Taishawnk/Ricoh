import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'

const el = document.getElementById('app')//modifys how the app is running to some dagree had to add this 
if (el){
    const data = {...el.dataset}//... is 
    console.log(data) //will need to reffrence where I want it render which in ths case is my main.html file just create a div a id of #app
    createApp(App, data).mount('#app') //will need to reffrence where I want it render which in ths case is my main.html file just create a div a id of #app
}//also added this if statement the only reason to do this is some we can add the console.log(el.dataset) data set is tide to the htmle that holds the id=app and allows
//me if neee to add a data-token ie <div id="app" data-token="1234567890"></div the data token and use it to get the token from the html file. more
//explicitly we actually want to pass in our csrf-token  so in reality it would look like this: <div id="app" data-token="{{csrf_token}}"></div>