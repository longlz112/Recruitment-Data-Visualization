import './assets/main.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from "@/router/index.js";
import * as echarts from 'echarts';
import axios from "axios";


const app=createApp(App)
app.use(router)
app.mount('#app')
