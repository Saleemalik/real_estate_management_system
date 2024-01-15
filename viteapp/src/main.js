import { createApp } from 'vue'
import App from '@/App.vue'
import { registerPlugins } from '@core/utils/plugins'
import axios from 'axios'

// Styles
import '@core/scss/template/index.scss'
import '@styles/styles.scss'



// Create vue app
const app = createApp(App)

app.config.globalProperties.$axios = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '/api',
})
axios.defaults.baseURL = import.meta.env.VITE_API_BASE_URL || '/api'
  
const token = localStorage.getItem('token')
if (token) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
} else {
  axios.defaults.headers.common['Authorization'] = null
}

// Register plugins
registerPlugins(app)

// Mount vue app
app.mount('#app')
