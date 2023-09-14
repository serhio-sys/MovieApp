import { createRouter, createWebHistory } from 'vue-router'
import MoviesView from '../views/MoviesView.vue'
import LoginView from '../views/LoginView.vue'
import SignUpView from '../views/SignUpView.vue'
import DetailView from '../views/DetailView.vue'
import FavoriteView from '../views/FavoriteView.vue'

const routes = [
    {
        path: "/",
        name: "Home",
        component: MoviesView
    },
    {
        path: "/login/",
        name: "Login",
        component: LoginView
    },
    {
        path: "/sign-up/",
        name: "Sign-Up",
        component: SignUpView
    },
    {
        path: "/favorite/",
        name: "Favorite",
        component: FavoriteView
    },
    {
        path: "/movie/:id/",
        name: "Detail",
        component: DetailView
    }
];

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});

export default router;