import {createRouter, createWebHistory} from 'vue-router'
import Home from './views/Home.vue'
import Predictions from './views/Predictions.vue'
import Statistics from './views/Statistics.vue'

const routes = [

    {
        name: 'Home',
        path: '/',
        component: Home
    },
    {
        name: 'Predictions',
        path: '/predictions',
        component: Predictions
    },
    {
        name: 'Statistics',
        path: '/statistics',
        component: Statistics
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


export default router