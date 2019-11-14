import VueRouter from "vue-router";
import Announcements from "@/views/Announcements";
import Login from "@/views/Login";
import store from "@/store";
import AnnouncementDetail from "@/views/AnnouncementDetail";
import PageNotFound from "@/views/PageNotFound";


const ifNotAuthenticated = (to, from, next) => {
    if (!store.getters.isAuthenticated)
        next();
    else
        next(false);
};

const routes = [
    { path: '/', component: Announcements },
    { path: '/announcements', component: Announcements },
    { path: '/announcements/:announcementId', component: AnnouncementDetail, props: true },
    { path: '/login', component: Login, beforeEnter: ifNotAuthenticated },
    { path: '*', component: PageNotFound }
];


export default new VueRouter({ routes });