import { createApp } from 'vue';
import { createPinia, setMapStoreSuffix  } from 'pinia';
import { createMemoryHistory, createRouter } from 'vue-router';

// Style
import './assets/css/main.css';


// Views
import App from './App.vue';
import SearchView from './components/SearchView.vue';
import SelectFriendsView from './components/SelectFriendsView.vue';
import SharedGamesView from './components/SharedGamesView.vue';
import TestView from './components/TestView.vue';


//Store
setMapStoreSuffix("")
const pinia = createPinia()


// Router
const routes = [
    { path: '/', component: SearchView },
    { path: '/select_friends', component: SelectFriendsView },
    { path: '/shared', component: SharedGamesView }
];
export const router = createRouter({
  history: createMemoryHistory(),
  routes
});

// Start
const app = createApp(App)
app.use(pinia)
app.use(router)
app.mount('#app')


// Log
console.log("VUE BOOTSTRAP STARTED")
