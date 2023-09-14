import { createApp } from 'vue'
import './scss/style.scss'
import App from './App.vue'
import Router from "./router"
import store from './store/store'

const app = createApp( App );
app.use( Router );
app.use( store )
app.mount( '#app' );